from flask import Flask, redirect, url_for,render_template, request, session
import json
from auth import *
from exception_practice2 import *
from user import *
app = Flask(__name__)
app.secret_key = "@ali97319731ali@"
@app.route("/", methods=["POST", "GET"])
def home():

    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        password = request.form["password"]
        session["password"] = password
        return redirect(url_for("user"))



    else:


        return render_template("index.html", my_title="hw5 Practice 2 - Web Project")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["login_username"]
        session["login_username"] = username
        password = request.form["login_password"]
        session["login_password"] = password
        the_user = Authenticator(username, password)
        is_login = the_user.login(username, password)
        session["is_logged_in"] = is_login
        return redirect(url_for("show_login"))

    else:
        return render_template("login.html",my_title="web")



@app.route("/register")
def user():

    if "username" in session and "password" in session:
        username = session["username"]
        if username in open('specs.json'):
            raise UsernameAlreadyExists
        password = session["password"]
        the_user = Authenticator(username,password)
        the_user.add_user()
        return redirect(url_for("home"))

    else:
        return redirect(url_for("home"))


@app.route("/show")
def show():
    database = open('specs.json')
    file1 = database.read()
    dic = json.loads(file1)
    database.close()

    return render_template("show.html",title_page="The Users Specs",dic=dic)

@app.route("/show_login")
def show_login():
    if "login_username" in session and "login_password" in session and "is_logged_in" in session :
        is_login = session["is_logged_in"]
        username = session["login_username"]
        password = session["login_password"]
        if username == "ali" and password == "123456789":
            return redirect(url_for("show"))
        else:

            return render_template("show_login.html", mytitle="Show Login",is_login=is_login,username=username)
    else:
        return redirect("login")
if __name__ == "__main__" :
    app.run(debug=True)
