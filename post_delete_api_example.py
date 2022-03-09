import requests
from pay_load import *
from utilities.resources import *
from utilities.configurations import *


# concatenation of endpoint
url_create_book = get_config()['API']['host'] + ApiResources.addBook
headers = {'Content-Type': 'application/json'}

# send post request and receive respond
add_book_response = requests.post(url_create_book, json=add_book_payload("123456719")
                                  , headers=headers, )

# convert JSON object respond to json
response_json = add_book_response.json()

# retrieve ID of book
book_id = response_json['ID']

# status code assertion
assert add_book_response.status_code == 200

# debugging
print(response_json)
print(book_id)
print(type(add_book_response))
print(add_book_response.json())
print('-----------------------------------------------')

# concatenation of endpoint for deleting book 'http://216.10.245.166/Library/DeleteBook.php'
url_delete_book = get_config()['API']['host'] + ApiResources.deleteBook


delete_book_response = requests.delete(url_delete_book, json={'ID': book_id})

assert delete_book_response.status_code == 200, "Status code is not 200 OK, book wasn't deleted"

delete_book_response_json = delete_book_response.json()
print(delete_book_response_json['msg'])
assert delete_book_response_json['msg'] == "book is successfully deleted", "Error with deleting a book"
