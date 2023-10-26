from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)



class Bill(db.Model):

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    ammount = db.Column(db.String(100))
    due_date = db.Column(db.Date())
    date_paid = db.Column(db.Date())
    is_paid = db.Column(db.Boolean())
    notes = db.Column(db.String(300))



    def __init__(self, bill):
        self.name = bill["name"][0]
        self.ammount = "ammount" in bill.keys()
        self.due_date = "due_date" in bill.keys()
        self.date_paid = "date_paid" in bill.keys()
        self.is_paid = bill["is_paid"][0]
        self.notes = bill["notes"][0]
