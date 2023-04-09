from flask import render_template, request, redirect
from app import app
from models.book_list import books, add_new_book, delete_book
from models.book import *

@app.route('/')
def index():
    return render_template('library.html', title='Home', books=books)

@app.route("/<int:id>")
def single_book(id):
    return render_template("archive.html", title="archive", book=books[id-1])

@app.route('/books', methods=['POST'])
def add_book():
  id = len(books) + 1
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  checked_out = 'checked_out' in request.form
  newbook = Book(id, title, author, genre, checked_out)
  add_new_book(newbook)
  return redirect('/')

@app.route('/books/delete/<title>', methods=['POST'])
def delete(title):
  delete_book(title)
  return redirect('/')