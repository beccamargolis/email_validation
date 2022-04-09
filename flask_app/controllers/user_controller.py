from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user_model import User

@app.route('/') #index route
def index():
    return render_template("index.html")

@app.route('/register',methods=['POST']) #action is to register the user
def register():
    if not User.validate_user(request.form): #if the validation fails,
        return redirect('/') #go back to index
    User.save(request.form) #otherwise, save the data to database,
    return redirect('/success') #and then display success page

@app.route('/success') #action is to show the successfully registered user
def success():
    users = User.get_all()
    return render_template("success.html", all_users = users)

@app.route('/user/delete/<int:id>') # delete user and redirect back to home
def destroy(id):
    User.destroy(id)
    return redirect('/success')