from flask import Flask, jsonify
import books_dao

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
books_dao = books_dao.BooksDAO()


@app.route('/')
def title_page():
    return jsonify(books_dao.get_all())

@app.route('/<int:book_id>')
def search_book_page(book_id):
    book = books_dao.get_by_id(book_id)
    return jsonify(book)

app.run()

