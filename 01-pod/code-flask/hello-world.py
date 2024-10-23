from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/tuncer')
def hello_tuncer():
    return '<h1>Hello, Tuncer!</h1>'

@app.route('/erdem')
def hello_erdem():
    return '<h1>Hello, Erdem!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
