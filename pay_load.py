def add_book_payload(isbn):
    body = {"name": "Search appium Automation with Python",
            "isbn": isbn,
            "aisle": "2223",
            "author": "John Smith"
            }
    return body
