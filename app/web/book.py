from flask import jsonify, request

from app.forms.book import SearchForm
from app.web import web
from app.libs.helper import is_isbn_or_key
from app.Spider.yushu_book import YuShuBook


@web.route("/book/search/")
def searcb():
    """
    q:普通关键字 isbn
    page
    ?q=金庸&page=1
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)

        return jsonify(result)
    else:
        return jsonify(form.errors)