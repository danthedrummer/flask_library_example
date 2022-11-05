from flask import Flask, render_template, request
import json

# env FLASK_APP=crud_api.py flask run
app = Flask(__name__)

# crud_client (python script) -> crud_api (flask app)
# browser -> flask app -> cat api

# This dictionary is like a fake database. It's a collection of data for us to interact with.
books_list = {
    "1": {"title": "Robots of Dawn"},
    "2": {"title": "Artemis"}, 
}
id_counter = 2


@app.route("/books", methods = ['GET', 'POST'])
def books():
    """
    Operating on the collection of books as a whole
    """
    # GET -> Fetch all books in the list
    if request.method == 'GET':
        return json.dumps(books_list, indent=2)

    # POST -> Create a new book in the list
    if request.method == 'POST':
        global id_counter
        id_counter = id_counter + 1
        books_list[id_counter] = request.json
        result = {
            "message": "New book created!",
            "book": books_list[id_counter],
        }
        return json.dumps(result, indent=2)


@app.route("/books/<book_id>", methods = ['GET', 'PUT', 'DELETE'])
def book(book_id):
    """
    Operating on a specific book from the collection
    
    :param book_id: The book_id path parameter
    """
    # GET -> Fetch a specific book by it's ID
    if request.method == 'GET':
        return json.dumps(books_list[book_id], indent=2)

    # PUT -> Update an existing book by it's ID
    if request.method == 'PUT':
        updated_book = request.json
        books_list[book_id] = updated_book
        result = {
            "message": "Book updated!",
            "book": updated_book,
        }
        return json.dumps(result, indent=2)
    
    # DELETE -> Remove a specific book from the list by it's ID
    if request.method == 'DELETE':
        if book_id in books_list:
            del books_list[book_id]
        return "Book deleted!"

