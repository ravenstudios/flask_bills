from __main__ import db
from flask_sqlalchemy import SQLAlchemy
import datetime



class Bill(db.Model):
    __tablename__ = "bill"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.Integer())
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
        self.paycheck_id = bill["paycheck_id"][0]

    def __repr__(self):
        return f"{self.name} {self.ammount}"

class Paycheck(db.Model):
    __tablename__ = "paycheck"
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.Integer())
    date_paid = db.Column(db.Date())
    # notes = db.Column(db.String(255))
    bills = db.relationship("Bill", backref="paycheck")




    def __init__(self, paycheck):
        self.name = paycheck["name"][0]
        self.ammount = paycheck["ammount"][0]
        self.date_paid = None
        self.notes = paycheck["notes"][0]
        # if paycheck.has_key('bills'):
        #     self.bills = paycheck["bills"][0]

    def __repr__(self):
        return f"{self.name} {self.ammount} {self.date_paid}"
