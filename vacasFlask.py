from datetime import datetime
from flask import Flask, flash, render_template as render, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cows.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class milk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    vaca = db.Column(db.Integer)
    litros = db.Column(db.Integer)

    def __init__(self, day, vaca, litros):
        self.day = day
        self.vaca = vaca
        self.litros = litros


@app.route('/', methods=['GET', 'POST'])
def home():
    milks = milk.query.all()
    print(milks)

    return render('index.html', milks=milks)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)