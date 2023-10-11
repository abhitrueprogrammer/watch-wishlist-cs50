from flask import Flask , render_template, flash, redirect, request, session
from helper import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash

# from flask_session import Session
# from werkzeug.security import check_password_hash, generate_password_hash
# Session(app)

import sqlite3
app = Flask(__name__)
db = sqlite3.connect("watch.db")
@app.route("/", methods=["POST", "GET"])
def index():
    # if request.method() == "POST":
    return render_template("index.html")
@app.route("/search")
def search():
    if request.method() == "GET":
        watches = db.execute("SELECT id, title FROM watch WHERE title LIKE ?", "%" + request.form.get("") + "%")
        return render_template("search.html", watches = watches)
    elif request.method() == "POST":
        number = 1
        watch_id = request.form.get("watchinfo")
        if request.form.get("type") == "cart":
            quote = lookup(watch_id)  #            "name": symbol, "price": price, "symbol": symbol
            if quote == None:
                return apology("symbol not found", 400)
            db.execute(
                "INSERT INTO purchase (user_id,symbol,quantity, price) VALUES(?,?,?,?);",
                session["user_id"],
                watch_id,
                number,
                quote["price"],
            )
            flash("Added to cart", category="message")
            return redirect("/search")
        elif request.form.get("type") == "info":
            watchinfo = lookup(watch_id)  #            "name": symbol, "price": price, "symbol": symbol
            if quote == None:
                return apology("symbol not found", 400)
            return render_template("info.html", watchinfo=watchinfo)
        # CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL, 
        # hash TEXT NOT NULL, cash NUMERIC NOT NULL DEFAULT 10000.00);

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username == ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        user = request.form.get("username")
        # Ensure username was submitted
        if not user:
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password and confirmation passwords are the same
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("The passwords do not match!", 400)
        if (
            db.execute("SELECT COUNT(*) FROM users WHERE username == ?", user)[0][
                "COUNT(*)"
            ]
            != 0
        ):
            return apology("Duplicate username!", 400)

            # TODO Display a warning instead of a new webpage.

        password_hash = generate_password_hash(request.form.get("password"))

        db.execute(
            "INSERT INTO users(username, hash) VALUES(?, ?)", user, password_hash
        )
        return render_template("success.html")
    else:
        return render_template("register.html")