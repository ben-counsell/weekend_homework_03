from models.book import Book

book_1 = Book('The Fellowship of the Ring', 'J.R.R. Tolkein', 'Fantasy', 1)
book_2 = Book('The Two Towers', 'J.R.R. Tolkein', 'Fantasy', 2)
book_3 = Book('The Return of the King', 'J.R.R Tolkein', 'Fantasy', 3)

books_list = [book_1, book_2, book_3]

def add_new_book(book):
    books_list.append(book)

def remove_book(catalogue_number):
    for book in books_list:
        if catalogue_number == book.catalogue_number:
            books_list.remove(book)