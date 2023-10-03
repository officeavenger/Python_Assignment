class Book:
    def _init_(self, id, title, author, price, rating):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

# Sample list of books
books = [
    Book(1, "Book 1", "Author 1", 19.99, 4.5),
    Book(2, "Book 2", "Author 2", 14.99, 3.8),
    Book(3, "Book 3", "Author 1", 12.99, 4.2),
    Book(4, "Book 4", "Author 3", 24.99, 4.8),
]

def find_book_by_id(books, id):
    for book in books:
        if book.id == id:
            return book
    return None

def find_books_by_author(books, author):
    matching_books = []
    for book in books:
        if book.author == author:
            matching_books.append(book)
    return matching_books

def find_books_in_rating_range(books, min_rating, max_rating):
    matching_books = []
    for book in books:
        if min_rating <= book.rating <= max_rating:
            matching_books.append(book)
    return matching_books

def find_books_in_price_range(books, min_price, max_price):
    matching_books = []
    for book in books:
        if min_price <= book.price <= max_price:
            matching_books.append(book)
    return matching_books

# Example usages:
book_found_by_id = find_book_by_id(books, 2)
print(book_found_by_id.title if book_found_by_id else "Book not found")

books_by_author = find_books_by_author(books, "Author 1")
for book in books_by_author:
    print(book.title)

books_in_rating_range = find_books_in_rating_range(books, 4.0, 4.5)
for book in books_in_rating_range:
    print(book.title)

books_in_price_range = find_books_in_price_range(books, 15.0, 20.0)
for book in books_in_price_range:
    print(book.title)