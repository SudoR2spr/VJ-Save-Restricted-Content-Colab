from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Back4apper!"

if __name__ == '__main__':
    app.run()
