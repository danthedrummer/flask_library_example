import json

from flask import Flask, request, Response

app = Flask(__name__)

# This dictionary is like a fake database. It's a collection of data for us to interact with.
books_list = {
    "1": {"title": "Robots of Dawn"},
    "2": {"title": "Artemis"},
}
id_counter = 2


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
        global id_counter
        id_counter = id_counter + 1
        books_list[str(id_counter)] = request.json
        result = {
            "message": "New book created!",
            "book": books_list[str(id_counter)],
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
        result = {
            "message": "Book updated!",
            "book": updated_book,
        }
        json_response = json.dumps(result, indent=2)
        return Response(json_response, status=200, mimetype='application/json')

    # DELETE -> Remove a specific book from the list by its ID
    if request.method == 'DELETE':
        print(book_id)
        print(books_list.keys())
        if book_id in books_list.keys():
            del books_list[book_id]
        return Response("Book deleted!", status=204, mimetype='application/json')
