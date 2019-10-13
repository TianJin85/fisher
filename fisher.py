from flask import Flask

from helper import is_isbn_or_key

app = Flask(__name__)

app.config.from_object('config')
@app.route("/book/search/<q>/<page>", methods=['GET', 'POST', 'delete'])
def searcb(q, page):

    is_isbn_or_key(q)


if __name__ == "__main__":

    app.run(
        host='0.0.0.0',
        debug=app.config['DEBUG'],
        port=5000
    )