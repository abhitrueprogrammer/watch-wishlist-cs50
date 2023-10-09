from flask import Flask , render_template, flash, redirect, request, session
# from flask_session import Session
# from werkzeug.security import check_password_hash, generate_password_hash
# Session(app)

import sqlite3
app = Flask(__name__)
con = sqlite3.connect("watch.db")
db = con.cursor()
@app.route("/", methods=["POST", "GET"])
def index():
    # if request.method() == "POST":
    return render_template("index.html")
@app.route("/search")
def search():
    watches = db.execute("SELECT id, title FROM watch WHERE title LIKE ?", "%" + request.form.get("") + "%")
    return render_template("search.html", watches = watches)