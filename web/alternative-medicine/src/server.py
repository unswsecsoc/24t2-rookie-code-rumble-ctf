from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "lmao"

try:
    os.remove("users.db")
except FileNotFoundError:
    pass

sqlite3.connect("users.db").cursor().execute("CREATE TABLE user(username, password, is_admin)")

@app.route("/")
def index():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        db = sqlite3.connect("users.db")
        cur = db.cursor()
        args = (request.form.get("username"), request.form.get("password"))
        data = cur.execute("SELECT username, password, is_admin FROM user WHERE username=? AND password=?", args).fetchone()
        if data is None:
            flash("Incorrect username or password", "danger")
        else:
            username, password, is_admin = data
            flash(f"Hello {username}!", "success")
            if is_admin:
                flash("Flag: BEGINNER{Ins3RT_InT0_tH3_InSER7_1NTo!!}", "success")
                flash("As part of our new security policy, your account will now be deleted", "success")
                cur.execute("DELETE FROM user WHERE username=?", (username,))
                db.commit()
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    code = None
    if request.method == "POST":
        if request.form.get("password") != request.form.get("confirm_password"):
            flash("Password and confirmation don't match", "danger")
        else:
            db = sqlite3.connect("users.db")
            cur = db.cursor()
            payload = f"INSERT INTO user (username, password, is_admin) VALUES (\"{request.form.get('username')}\", \"{request.form.get('password')}\", 0)"
            cur.execute(payload)
            db.commit()
            if request.form.get("debug", False):
                code = payload

            flash("Successfully registered user!", "success")
    return render_template("register.html", code=code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9999)
