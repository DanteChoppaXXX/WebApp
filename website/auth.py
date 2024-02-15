from flask import Blueprint, render_template, request, flash

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
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 4 characters!", category="error")
        elif len(firstName) < 2:
            flash("First name must be greater than 1 characters!", category="error")
        elif len(lastName) < 2:
            flash("Last name must be greater than 1 characters!", category="error")
        elif password1 != password2:
            flash("Passwords doesn't match!", category="error")
        elif len(password2) < 7:
            flash("Password must be at least 7 characters!", category="error")
        else:
            flash("Account Created!", category="success")
            # Add user to database
        data = request.form
        print(data)

    return render_template("signup.html")
    