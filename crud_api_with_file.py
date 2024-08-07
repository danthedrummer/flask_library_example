import json
import os
import uuid

from flask import Flask, request, Response

# Quick explanation of the "json" package:
#
# json.loads transforms a JSON string into a Python dictionary
#
# json.dumps transforms a Python dictionary into a JSON string
#   This also optionally allows a parameter called "indent" which
#   prints the JSON string with nice spacing, so it's readable.

app = Flask(__name__)

# This dictionary is like a fake database. It's a collection of data for us to interact with.
books_list = {}
if os.path.exists("books.json"):
    # if the books.json file exists then read from it
    with open('books.json', 'r') as file:
        books_list = json.load(file)
else:
    # else we create a new file and write an empty dictionary to it
    with open("books.json", 'w') as file:
        file.write(json.dumps(books_list))


def update_file():
    """
    Updates the books.json file with the current contents of the books_list variable
    """
    with open("books.json", 'w') as file:
        file.write(json.dumps(books_list, indent=2))


@app.route("/books", methods=['GET', 'POST'])
def books():
    """
    Operating on the collection of books as a whole
    """
    # GET -> Fetch all books in the list
    if request.method == 'GET':
        json_response = json.dumps(books_list, indent=2)
        return Response(json_response, status=200, mimetype='application/json')

    # POST -> Create a new book in the list
    if request.method == 'POST':
        new_id = str(uuid.uuid1())  # UUIDs are just random generated strings
        books_list[new_id] = request.json
        update_file()
        result = {
            "message": "New book created!",
            "book": books_list[new_id],
        }
        json_response = json.dumps(result, indent=2)
        return Response(json_response, status=201, mimetype='application/json')


@app.route("/books/<book_id>", methods=['GET', 'PUT', 'DELETE'])
def book(book_id):
    """
    Operating on a specific book from the collection
    
    :param book_id: The book_id path parameter
    """
    # GET -> Fetch a specific book by its ID
    if request.method == 'GET':
        json_response = json.dumps(books_list[book_id], indent=2)
        return Response(json_response, status=200, mimetype='application/json')

    # PUT -> Update an existing book by its ID
    if request.method == 'PUT':
        updated_book = request.json
        books_list[book_id] = updated_book
        update_file()
        result = {
            "message": "Book updated!",
            "book": updated_book,
        }
        json_response = json.dumps(result, indent=2)
        return Response(json_response, status=200, mimetype='application/json')

    # DELETE -> Remove a specific book from the list by its ID
    if request.method == 'DELETE':
        if book_id in books_list.keys():
            del books_list[book_id]
            update_file()
        return Response("Book deleted!", status=204, mimetype='application/json')
