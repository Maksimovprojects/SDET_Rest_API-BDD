import requests
import json

response = requests.get('http://216.10.245.166/Library/GetBook.php',
                        params={'AuthorName': 'Rahul Shetty2'}, )

# print(response.text)
# print(type(response.text))
# response_str = response.text
# dict_response = json.loads(response_str)
# print(dict_response[0]['aisle'])

json_response = response.json()
# print(type(json_response))
# print(json_response[2]['aisle'])
# print(response.json())
# print(response.status_code)

print(response.headers)
assert response.status_code == 200, "Status code isn't 200"

# Retrieve the book details with ISBN having value 'RGHCC'
expected_book = {
    'book_name': 'Learn Appium Automation with Java',
    'isbn': 'RGHCC',
    'aisle': '99755'
}

for book in json_response:
    if book['aisle'] == '99755':
        print(book)
        actual_book = book

assert actual_book == expected_book, "Error, different book"
print('test passed')
print('-----------------------------------------------------')


