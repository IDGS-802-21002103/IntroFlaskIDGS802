from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    '''Funcion inicial de la aplicacion'''
    return '<p>Hello, World!<p>'

if __name__ == '__main__':
    app.run()
