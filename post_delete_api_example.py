import requests
from pay_load import *
from utilities.configurations import *


# send post request and receive respond
add_book_response = requests.post(get_config()['API']['host']+'/Library/Addbook.php', json=add_book_payload("123456719")
                                  , headers={'Content-Type': 'application/json'}, )

# convert JSON object respond to json
response_json = add_book_response.json()

# retrieve ID of book
book_id = response_json['ID']

# status code assertion
assert add_book_response.status_code == 200

# debugging
print(book_id)
print(type(add_book_response))
print(add_book_response.json())
print('-----------------------------------------------')

delete_book_response = requests.delete('http://216.10.245.166/Library/DeleteBook.php', json={'ID': book_id})

assert delete_book_response.status_code == 200, "Status code is not 200 OK, book wasn't deleted"

delete_book_response_json = delete_book_response.json()
print(delete_book_response_json['msg'])
assert delete_book_response_json['msg'] == "book is successfully deleted", "Error with deleting a book"
