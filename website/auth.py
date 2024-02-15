from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        print(data)
        return render_template("home.html")
    else:
        return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>You've Logged Out!</p>"

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        return render_template("login.html")
    else:
        return render_template("signup.html")