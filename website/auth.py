from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["POST", "GET"])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>You've Logged Out!</p>"

@auth.route('/signup', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        return render_template("login.html")
    else:
        return render_template("signup.html")