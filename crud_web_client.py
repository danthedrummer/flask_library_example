from flask import Flask, request, render_template

# pipenv run flask --app crud_web_client.py run
app = Flask(__name__)

# This dictionary is like a fake database. It's a collection of data for us to interact with.
books_list = {
    "1": {"id": "1", "title": "Robots of Dawn"},
    "2": {"id": "2", "title": "Artemis"},
}
id_counter = 2


@app.route('/')
def library():
    return render_template("library.html.j2")


@app.route('/books/create')
def create_book():
    return render_template("add_book.html.j2")


@app.route("/books", methods=['GET', 'POST'])
def books():
    """
    Operating on the collection of books as a whole
    """
    # POST -> Create a new book in the list
    if request.method == 'POST':
        global id_counter
        id_counter = id_counter + 1
        new_book = dict(request.form)
        new_book['id'] = str(id_counter)
        books_list[str(id_counter)] = new_book

    return render_template("books.html.j2", books=books_list.values())


@app.route("/books/<book_id>", methods=['GET'])
def book(book_id):
    """
    Operating on a specific book from the collection

    :param book_id: The book_id path parameter
    """
    # GET -> Fetch a specific book by its ID
    if request.method == 'GET':
        return render_template("book.html.j2", book=books_list[book_id])
