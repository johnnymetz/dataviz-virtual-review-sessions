from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Welcome to the index page!'

@app.route('/')
def index():
    characters = [
        {'name': 'Darth Vader', 'force': 'Dark'},
        {'name': 'Yoda', 'force': 'Light'},
        {'name': 'Luke Skywalker', 'force': 'Light'}
    ]
    return render_template('index.html', author='DataViz class', characters=characters)

@app.route('/<name>')
def welcome(name):
    return f'Welcome {name}!'

@app.route('/<name>/<int:age>')
def future_age(name, age):
    return f'Welcome {name}! In five years you will be {age + 5} years old'

if __name__ == '__main__':
    app.run(debug=True)
