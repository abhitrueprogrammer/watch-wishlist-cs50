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
    if request.method() == "POST":
        
    return render_template("index.html")
# @app.route("/selection")
# def selection():
#     return render_template("selection.html")
# log in blyat
# if index.method == get():
#     return index.html
# else:
#     method.get("POST"):
#         lst = input.get)
#     return("index.html", lst)
# elseif:
#     query.click"XYZ"
#     lst_of_disc = sql.execute("FROM DB GET XYZ") #, other discription
#     url = imageapi.search(lst_of_disc.name)
#     lst_of_disc["url"] = url
#     return("Product Discription.html",lst_of_disc)
# @productDisc.html
# if method.get == "POST":
#     get.watchid()
#     sql.execute("INSERT INTO DB wishlist VALUES(watch_id, quantity++)")
# cart:
#     if method == "GET":
#     lst_of_disc = sql.execute("FROM DB wishlist, product_disc GET XYZ") #, other discription
#     return("cart.html", lst_of_disc)
# #Implement admin and user login. Admin can add watch info in db. get and then INSERT INTO DB 