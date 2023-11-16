from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from __main__ import app
from schema import db, Bill, Paycheck
import datetime



@app.route('/')
def index():
    return render_template('paycheck/show-paychecks.html', paychecks=Paycheck.query.all())



@app.route('/show-paychecks', methods = ['GET', 'POST'])
def show_paychecks():
    return render_template('paycheck/show-paychecks.html', bills=Bill.query.all(), paychecks=Paycheck.query.all())



@app.route('/add-new-paycheck-form', methods = ['GET', 'POST'])
def add_new_paycheck_form():
    if request.method == 'POST':
        id = request.args.get('_id')
        return render_template('paycheck/paycheck-form.html', paycheck=Paycheck.query.get(id))
    else:
        return render_template('paycheck/paycheck-form.html', today=datetime.datetime.now().strftime("%Y-%m-%d"))



@app.route('/add-new-paycheck', methods = ['GET', 'POST'])
def add_new_paycheck():
    form_data = request.form.to_dict(flat=False)
    new_paycheck = Paycheck(form_data)
    date_arr = form_data["date-paid"][0].split("-")
    date_paid = datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
    new_paycheck.date_paid = date_paid
    db.session.add(new_paycheck)
    db.session.commit()
    return redirect("/show-paychecks")


@app.route('/edit-paycheck-form', methods = ['GET', 'POST'])
def edit_paycheck_form():
    id = request.args.get('_id')
    return render_template('paycheck/paycheck-form.html', paycheck=Paycheck.query.get(id))


@app.route('/edit-paycheck', methods = ['GET', 'POST'])
def edit_paycheck():
    form_data = request.form.to_dict(flat=False)
    paycheck = Paycheck.query.get(form_data["_id"])
    paycheck.name = form_data["name"][0]
    paycheck.ammount = form_data["ammount"][0]
    date_arr = form_data["date-paid"][0].split("-")
    date = datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
    paycheck.date_paid = date
    paycheck.notes = form_data["notes"][0]
    db.session.commit()
    return render_template('paycheck/show-paychecks.html', paychecks=Paycheck.query.all())



@app.route('/delete-paycheck', methods = ['GET', 'POST'])
def delete_paycheck():
    args = request.args
    Paycheck.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/show-paychecks")



# *******************Bills**************************
@app.route('/show-bills', methods = ['GET', 'POST'])
def show_bills():
    return render_template('bill/show-bills.html', bills=Bill.query.all())



@app.route('/add-new-bill-form', methods = ['GET', 'POST'])
def add_new_bill_form():
    if request.method == 'POST':
        if request.arge.get('paycheck-id'):
            return render_template('bill/bill-form.html', paycheck=Paycheck.query.get(id))

        else:
            id = request.args.get('_id')
            return render_template('bill/bill-form.html', bill=Bill.query.get(id))
    else:
        return render_template('bill/bill-form.html', today=datetime.datetime.now().strftime("%Y-%m-%d"))



@app.route('/add-new-bill', methods = ['GET', 'POST'])
def add_new_bill():
    form = request.form.to_dict(flat=False)
    db.session.add(Bill(form))
    db.session.commit()
    return redirect("/")



@app.route('/edit-bill-form', methods = ['GET', 'POST'])
def edit_bill_form():
    id = request.args.get('_id')
    print(f"id:{id}")
    return render_template('bill/bill-form.html', bill=Bill.query.get(id), paychecks=Paycheck.query.all())



@app.route('/edit-bill', methods = ['GET', 'POST'])
def edit_bill():
    form_data = request.form.to_dict(flat=False)
    bill = Bill.query.get(form_data["_id"])
    bill.name = form_data["name"][0]
    bill.ammount = form_data["ammount"][0]
    bill.notes = form_data["notes"][0]
    date_arr = form_data["due-date"][0].split("-")
    date = datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))
    bill.due_date = date
    bill.paycheck_id = form_data["paycheck_id"][0]
    db.session.commit()
    return render_template('bill/show-bills.html', bills=Bill.query.all())


@app.route('/paid-bill', methods = ['GET', 'POST'])
def paid_bill():
    id = request.args.get('_id')
    bill = Bill.query.get(id)
    bill.date_compleated = datetime.datetime.now()
    bill.is_paid = True
    db.session.commit()
    return render_template('bill/show-bills.html', bills=Bill.query.all())



@app.route('/unpay-bill', methods = ['GET', 'POST'])
def unpay_bill():
    id = request.args.get('_id')
    bill = Bill.query.get(id)
    bill.date_compleated = None
    bill.is_paid = False
    db.session.commit()
    return render_template('bill/show-bills.html', bills=Bill.query.all())


@app.route('/delete-bill', methods = ['GET', 'POST'])
def delete_bill():
    args = request.args
    Bill.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/")



@app.route('/remove-bill', methods = ['GET', 'POST'])
def remove_bill():
    id = request.args.get('_id')
    bill = Bill.query.get(id)
    bill.paycheck_id = None
    db.session.commit()
    return redirect("/")
