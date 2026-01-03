from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'title': 'Robinzone  Cruzo One',
     'author': 'Author One',
     'category': 'science'},
    {'title': 'Title Two',
     'author': 'Author Two',
     'category': 'science'},
    {'title': 'Title Three',
     'author': 'Author Three',
     'category': 'history'},
    {'title': 'Robinzone p2',
     'author': 'Author Four',
     'category': 'math'},
    {'title': 'Title Five Robic',
     'author': 'Author Four',
     'category': 'math'},
    {'title': 'Robinzone Returns',
     'author': 'Author Two',
     'category': 'math'}
]


# @app.get("/books")
# async def read_all_books():
#     return BOOKS


# @app.get("/books/{id}")
# async def read_book(id: int):
#     return BOOKS[id]


# @app.get("/books/{book_title}")
# async def get_book_by_title(book_title: str):
#     for book in BOOKS:
#         if book.get('title').casefold() == book_title.casefold():
#             return book
#
#
# @app.get("/authors")
# async def get_author_by_name(author_name: str):
#     for book in BOOKS:
#         if book.get('author').casefold() == author_name.casefold():
#             return book


# @app.get("/books/")
# async def get_books_by_category(cat: str):
#     books_by_category = []
#
#     for book in BOOKS:
#         if book.get('category').casefold() == cat.casefold():
#             books_by_category.append(book)
#
#     return books_by_category

# @app.get("/books/")
# async def get_books_by_category_and_author(cat: str, author: str):
#     result_books= []
#
#     for book in BOOKS:
#         if book.get('category').casefold() == cat.casefold() and book.get('author').casefold() == author.casefold():
#             result_books.append(book)
#
#     return result_books


@app.get("/books/")
async def get_searched_book(s: str, limit: int):
    searched_books = []
    book_counter = 0

    for book in BOOKS:
        if s.casefold() in book.get('title').casefold():
            searched_books.append(book)
            book_counter += 1

            if book_counter == limit:
                break

    return searched_books