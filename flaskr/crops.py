import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flaskr.db import get_db
from flaskr.users import login_required

crops_route = Blueprint('crops', __name__)

@crops_route.route('/crops', methods = ["GET", "POST"])
@login_required
def show_crops():
    if request.method =="GET":
        db = get_db()
        crops = db.execute("SELECT * FROM crops WHERE user_id = ?",(session['user_id'],)).fetchall()
        return render_template("crops.html", crops = crops)
 
 
@crops_route.route('/newcrop', methods = ["GET", "POST"])
@login_required
def new_crop():
    if request.method =="GET":
        return render_template("newcrop.html")
    else:
        db=get_db()
        cropname = request.form.get("cropname")
        cropbreed = request.form.get("cropbreed")
        user_id = session['user_id']
        
        db.execute("INSERT INTO crops (user_id,cropname,cropbreed) VALUES (?,?,?)", (user_id,cropname, cropbreed))
        db.commit()
        
        return redirect ('/crops')