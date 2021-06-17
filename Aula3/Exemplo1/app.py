from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, Flask!</h1>"

if (__name__ == 'main'):
    app.run(debug=True)