from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Darya Belka!"


@app.route('/name/<name>')
def name(name=None):
        return f'Hello, {name}!'