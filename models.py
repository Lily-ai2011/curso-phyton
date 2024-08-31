from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Dogs(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    color = db.Column(db.String(20))
    race = db.Column(db.String(20))
    size = db.Column(db.String(20))
    conduct = db.Column(db.String(150))
    personality = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)

class Solicitud(db.Model):
    id = db.Column(db.Integer, primary_key = True)