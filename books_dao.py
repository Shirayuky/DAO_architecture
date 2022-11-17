import json
from typing import List

PATH = 'books.json'

class BooksDAO:
    def star_load(self):
        return self.load_data_fron_json(PATH)

    def load_data_fron_json(self, path: str) -> List[dict]:
        with open(path, 'r', encoding='utf-8') as file:
            books = json.load(file)
            return books

    def get_all(self):
        return self.star_load()

    def get_by_id(self, book_id):
        books = self.star_load()
        for book in books:
            if book['pk'] == book_id:
                return book


