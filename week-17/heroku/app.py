from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecret'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))

    def __repr__(self):
        return '<{}>'.format(self.title)


@app.route('/', methods=['GET'])
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@app.route('/add_todo', methods=['POST'])
def add_todo():
    todo = Todo(title=request.form['title'], description=request.form['description'])
    db.session.add(todo)
    db.session.commit()
    flash('Todo successfully added!', category='success')
    return redirect(url_for('index'))


@app.route('/delete_todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo successfully deleted!', category='warning')
    return redirect(url_for('index'))


if __name__ == '__main__':
    import threading, webbrowser
    threading.Timer(2, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    app.run()
