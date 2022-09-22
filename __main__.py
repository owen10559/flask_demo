import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello, flask.\n"

if __name__ == '__main__':
    app.run("0.0.0.0")
