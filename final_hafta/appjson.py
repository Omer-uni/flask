from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), default='İnceleme Bekliyor')
    file = db.Column(db.String(200))

def export_users_to_json():
    with app.app_context():
        users = User.query.all()
        data = [{
            'id': user.id,
            'firstname': user.firstname,
            'lastname': user.lastname,
            'email': user.email,
            'password': user.password
        } for user in users]

        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

def export_tickets_to_json():
    with app.app_context():
        tickets = Ticket.query.all()
        data = [{
            'id': t.id,
            'firstname': t.firstname,
            'lastname': t.lastname,
            'email': t.email,
            'subject': t.subject,
            'message': t.message,
            'priority': t.priority,
            'status': t.status,
            'file': t.file,
        } for t in tickets]

        with open('tickets.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    export_users_to_json()
    export_tickets_to_json()
    print("Veriler başarıyla export edildi.")
