@app.route('/')
def index():
    return render_template('index.html', shopping_list=Shopping_list.query.all())



@app.route('/add-new-item', methods = ['POST'])
def add_new_item():
    db.session.add(Shopping_list(request.json["item"]))
    db.session.commit()
    return redirect("/")



@app.route('/delete-item', methods = ['POST'])
def delete():
    Shopping_list.query.filter_by(_id=request.json["id"]).delete()
    db.session.commit()
    return redirect("/")
