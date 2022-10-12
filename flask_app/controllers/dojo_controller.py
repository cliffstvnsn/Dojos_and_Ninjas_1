from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo_model import Dojo

@app.route('/')
@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojos.html", all_dojos=all_dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create(request.form)
    print(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def dojoshow(id):
    data = {
        "id":id
        }
    return render_template("dojoshow.html", dojo = Dojo.get_one(data))
