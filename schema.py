from __main__ import app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy(app)



class Bill(db.Model):

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.String(100))
    due_date = db.Column(db.Date())
    date_paid = db.Column(db.Date())
    is_paid = db.Column(db.Boolean())
    notes = db.Column(db.String(300))
    paycheck_id = db.Column(db.Integer, db.ForeignKey("paycheck._id"))



    def __init__(self, bill):
        self.name = bill["name"][0]
        self.ammount = bill["ammount"][0]
        self.due_date = datetime.datetime.now()
        self.date_paid = None
        self.is_paid = None
        self.notes = bill["notes"][0]


class Paycheck(db.Model):

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.String(100))
    paid_date = db.Column(db.Date())
    bills = db.relationship("Bill", backref="bill")



    def __init__(self, paycheck):
        self.name = paycheck["name"][0]
        self.ammount = paycheck["ammount"][0]
        self.due_date = datetime.datetime.now()
        self.date_paid = None
        self.is_paid = None
        self.notes = paycheck["notes"][0]
        self.bills = []
