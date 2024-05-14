from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Stocks(db.Model): #Blueprint for all stocks to follow this 
    id = db.Column(db.Integer, primary_key=True)
    tracker = db.Column(db.String(7)) #7 max string to follow ticker sign 
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #Needs an existing user to be able to store these


class User(db.Model, UserMixin): #Blueprint for all users to follow this
    id = db.Column(db.Interger,  primary_key = True) #Primary key is used to differentiate between same info ie Names/Usernames/emails  
    email = db.Column(db.String(100), unique = True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(100))
    stocks = db.relationship('Stocks') 