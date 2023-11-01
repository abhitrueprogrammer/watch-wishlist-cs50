from flask import redirect, render_template, session
from functools import wraps
import sqlite3
from google_images_search import GoogleImagesSearch

db = sqlite3.connect("watch.db", check_same_thread=False)
gis = GoogleImagesSearch('AIzaSyC5uNFp0zfvsDeHg_6CA-F79ssycywQHX8', '35ed6304d1c67415a')

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
def apology(warning, code):
    return render_template("apology.html", warning = warning, code = code)
def watchExists(watchid):
    # Was lookup function
    id = db.execute("SELECT id FROM watches WHERE id == ?", (watchid,)).fetchall()
    if id == []:
        print("Image does not exist")
        return False
    else:
        return True
def get_image_url(query):
    print(query)
    _search_params = {
    'q'       : query,
    'num'     : 1,
    'safe'    : 'high',
    'fileType': 'jpg|png',
    'imgType' : 'photo',
    }
    gis.search(search_params=_search_params)
    for image in gis.results():
        return image.url
def update_watch_url():
    basket = db.execute("SELECT id, watchname, image_url FROM watches").fetchall()
    for row in basket:
        if row[2] == None: ##<-- do NOT fuck this up 
                db.execute("""
        UPDATE watches
        SET image_url = ?
        WHERE
        id == ?""", (get_image_url(row[1]),row[0]))
    db.commit()
if __name__ == "__main__":
    update_watch_url()