# REST API Sample Project

This is a basic sample project which emulates a library which is storing a collection of books which can be interacted
with via REST requests.

## Pipenv

The project uses pipenv with all of the necessary packages declared in the `Pipfile`. Install all of the packages needed
by running:
> pipenv sync

## The Servers

### `crud_api.py`

This is a basic CRUD API built with Flask that supports creating, requesting, updating, and deleting books from the
library. This script will reset when the server is shut down and restarted so changes to the library are volatile.

Start server by running:
> pipenv run flask --app crud_api.py run

### `crud_api_with_file.py`

This is the same as `crud_api.py` but the information is backed by a file so the information is retained between server
restarts. The changes to the library are non-volatile. After running the script for the first time you will see
a `books.json` file appear in the project which acts as an imposter "database".

Start server by running:
> pipenv run flask --app crud_api_with_file.py run

## The Clients

Once the servers are running then we can interact with them using whichever clients we prefer. Here's 2 options, but you
can also build your own if you prefer!

### `crud_client.py`

Simple command line interface (CLI) app which allows simple interactions with whichever `crud_api` server is running.
Uses the `requests` Python module for sending REST requests.

Start client by running:
> pipenv run python crud_cli_client.py

### `cURL`

We can interact directly using `cURL` which is not as user-friendly but gives us greater control over the requests we
send.

GET all books
> curl http://localhost:5000/books

GET book by id
> curl http://localhost:5000/books/{id}

POST create book
> curl -X POST -d '{"name": "Ubik"}' -H "Content-Type: application/json" http://localhost:5000/books

PUT update book by id
> curl -X PUT -d '{"name": "Brave New World"}' -H "Content-Type: application/json" http://localhost:5000/books/{id}

DELETE remove book by id
> curl -X DELETE http://localhost:5000/books/{id}
 
## Web client

### `crud_web_client.py`

This is a server and a client combined. It behaves similarly to `crud_api.py` in that it manages the data for the 
library internally, but it serves HTML instead of JSON so the contents can be navigated in a web browser. HTML doesn't
natively support PUT or DELETE requests so this client can only create books but this functionality can be implemented
in other ways.

Start this client by running
> pipenv run flask --app crud_web_client.py run
