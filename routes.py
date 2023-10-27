from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from __main__ import app
from schema import db, Bill, Paycheck


@app.route('/')
def index():
    return render_template('show-bills.html', bills=Bill.query.all())



@app.route('/show-paychecks', methods = ['GET', 'POST'])
def show_paychecks():
    return render_template('show-paychecks.html', bills=Bill.query.all(), paychecks=Paycheck.query.all())



@app.route('/show-bills', methods = ['GET', 'POST'])
def show_bills():
    return render_template('show-bills.html', bills=Bill.query.all())







@app.route('/add-new-paycheck-form', methods = ['GET', 'POST'])
def add_new_paycheck_form():
    return render_template('add-new-paycheck-form.html')



@app.route('/add-new-paycheck', methods = ['GET', 'POST'])
def add_new_paycheck():
    form_data = request.form.to_dict(flat=False)
    new_paychack = Paycheck(form_data)
    db.session.add(new_paychack)
    db.session.commit()
    return redirect("show-paychecks")


@app.route('/edit-paycheck-form', methods = ['GET', 'POST'])
def edit_paycheck_form():
    print("edit paycheck form ")
    id = request.args.get('_id')
    return render_template('edit-paycheck-form.html', paycheck=Paycheck.query.get(id))


@app.route('/edit-paycheck', methods = ['GET', 'POST'])
def edit_paycheck():
    form = request.form.to_dict(flat=False)
    print(form)
    paycheck = Paycheck.query.get(form["_id"])
    paycheck.name = form["paycheck-name"][0]
    paycheck.ammount = form["paycheck-ammount"][0]
    paycheck.notes = form["notes"][0]
    db.session.commit()
    return render_template('show-paychecks.html', paychecks=Paycheck.query.all())



@app.route('/delete-paycheck', methods = ['GET', 'POST'])
def delete_paycheck():
    args = request.args
    Paycheck.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/show-paychecks")




@app.route('/add-new-bill-form', methods = ['GET', 'POST'])
def add_new_bill_form():
    return render_template('add-new-bill-form.html', paychecks=Paycheck.query.all())



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
    return render_template('edit-bill-form.html', bill=Bill.query.get(id), paychecks=Paycheck.query.all())



@app.route('/edit-bill', methods = ['GET', 'POST'])
def edit_bill():
    form = request.form.to_dict(flat=False)
    bill = Bill.query.get(form["_id"])
    bill.name = form["bill-name"][0]
    bill.ammount = form["bill-ammount"][0]
    bill.notes = form["notes"][0]
    bill.paycheck_id = form["paycheck_id"][0]
    db.session.commit()
    return render_template('show-bills.html', bills=Bill.query.all())


@app.route('/compleated-bill', methods = ['GET', 'POST'])
def compleated_bill():
    id = request.args.get('_id')
    bill = Bill.query.get(id)
    bill.date_compleated = datetime.datetime.now()
    bill.compleated = True
    db.session.commit()
    return render_template('index.html', bill=Bill.query.all())



@app.route('/delete-bill', methods = ['GET', 'POST'])
def delete_bill():
    args = request.args
    Bill.query.filter_by(_id=args.get("_id")).delete()
    db.session.commit()
    return redirect("/")
