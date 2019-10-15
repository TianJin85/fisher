from flask import jsonify, request

from app.web import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route("/book/search/")
def searcb():
    """
    q:普通关键字 isbn
    page
    ?q=金庸&page=1
    :return:
    """
    q = request.args["q"]
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_isbn(q)

    return jsonify(result)