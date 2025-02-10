import json

book = {"title": "History", "author": "John", "Year": 1991, "Chapters": {1:"America", 2:"Europe", 3:"Asia"}}

with open("book.json", "w") as f:
    json.dumps(book, f)






