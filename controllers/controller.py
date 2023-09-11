from flask import render_template, Blueprint, request, redirect
from models.book import Book
from models.book_list import books_list, add_new_book, remove_book

book_blueprint = Blueprint('books', __name__)

used_catalogue_numbers = [1, 2, 3]

@book_blueprint.route('/books')
def index():
    return render_template('index.jinja', title='List of Books', books=books_list)

@book_blueprint.route('/books/<int:catalogue_number>')
def get_book_details(catalogue_number):
    for book in books_list:
        if catalogue_number == book.catalogue_number:
            return render_template('book_details.jinja', title='Book detail', book=book)
    else:
        return 'Error: book not found'
    
@book_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    
    sorted_list = sorted(used_catalogue_numbers)
    catalogue_number = sorted_list[-1] + 1
    used_catalogue_numbers.append(catalogue_number)

    new_book = Book(title, author, genre, catalogue_number)
    add_new_book(new_book)
    return redirect('/books')

@book_blueprint.route('/books/delete/<int:catalogue_number>', methods=['POST'])
def delete(catalogue_number):
    remove_book(catalogue_number)
    return redirect('/books')