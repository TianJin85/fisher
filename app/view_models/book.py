# -*- encoding: utf-8 -*-
"""
@File    : book.py
@Time    : 2019/10/29 9:22
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.isbn = book['isbn']
        self.pages = book['pages']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return '/'.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel:
    @classmethod
    def pacage_single(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': ''
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls._cut_book_data(data)]
            return returned

    @classmethod
    def pacage_collection(cls, data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data['books'])
            returned['books'] = [cls._cut_book_data(book) for book in data['books']]
            return returned

    @classmethod
    def _cut_book_data(cls, data):

        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
