from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def ninjas():
    all_dojos = Dojo.get_all()
    return render_template('ninjas.html', all_dojos=all_dojos)

@app.route('/ninjas/create', methods=['POST'])
def create():
    Ninja.create_ninja(request.form)
    print(request.form)
    return redirect(f'/dojos/{request.form["dojo_id"]}')


