import requests
import json

# Quick explanation of the "json" package:
#
# json.loads transforms a JSON string into a Python dictionary
#
# json.dumps transforms a Python dictionary into a JSON string
#   This also optionally allows a parameter called "indent" which
#   prints the JSON string with nice spacing so it's readable.

def get_all_books():
    """
    GET request to fetch all books
    """
    response = requests.get("http://127.0.0.1:5000/books")
    print(json.loads(response.content))


def create_new_book(title):
    """
    POST request to create a new book
    """
    response = requests.post(
        url="http://127.0.0.1:5000/books",
        json={"title": title },
        headers={"Content-Type": "application/json"}
    )
    print(json.loads(response.content))


def get_book(book_id):
    """
    GET request to fetch a specific book
    """
    response = requests.get(f"http://127.0.0.1:5000/books/{book_id}")
    print(json.loads(response.content))


def update_book(book_id, new_title):
    """
    PUT request to update an existing book
    """
    response = requests.put(
        url=f"http://127.0.0.1:5000/books/{book_id}",
        json={"title": new_title },
        headers={"Content-Type": "application/json"}
    )
    print(response.content)


def delete_book(book_id):
    """
    DELETE request to delete an existing book
    """
    response = requests.delete(f"http://127.0.0.1:5000/books/{book_id}")
    print(response.content)


if __name__ == "__main__":
    while True:
        print("=======================================================")
        print("| Welcome to our library! View available options below:")
        print("| 1. View all books")
        print("| 2. View specific book")
        print("| 3. Donate new book")
        print("| 4. Update existing book")
        print("| 5. Delete existing book")
        print("| Type anything else to exit")
        print("========================================================\n")
        choice = input("What would you like to do?\n")

        if choice == "1":
            get_all_books()

        elif choice == "2":
            book_id = input("What is the ID of the book you want to see?\n")
            get_book(book_id)

        elif choice == "3":
            title = input("What is the name of the new book?\n")
            create_new_book(title)

        elif choice == "4":
            book_id = input("What is the ID of the book you wish to update?\n")
            new_title = input("What is the book's new title?\n")
            update_book(book_id, new_title)

        elif choice == "5":
            book_id = input("what is the ID of the book you wish to delete?\n")
            delete_book(book_id)

        else:
            break