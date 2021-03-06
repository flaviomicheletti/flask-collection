from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("foo")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email    = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email    = email

    def __repr__(self):
        return '<User %r>' % self.username
    
@app.route("/")
def hello_model():
    user = User.query.filter_by(id=1).first()
    return "Hello user %s!" % user.username

if __name__ == "__main__":
    app.run(debug=True)
