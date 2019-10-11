from flask import Flask, make_response

app = Flask(__name__)

app.config.from_object('config')
@app.route("/hello", methods=['GET', 'POST', 'delete'])
def hello():
    li = {"name": "Tianjin"}
    return li


if __name__ == "__main__":

    app.run(
        host='0.0.0.0',
        debug=app.config['DEBUG'],
        port=5000
    )