import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flaskr.db import get_db
from flaskr.users import login_required

farmsdetails_route = Blueprint('farmdetails', __name__)

#Route to display list of crops in the select section. Crops taken from crops database
@farmsdetails_route.route("/farmdetails", methods =["GET", "POST"])
@login_required
def farmdetails():
    if request.method == "GET":
        db = get_db()
        crops = db.execute("SELECT cropname, cropbreed FROM crops WHERE user_id = ? ORDER BY cropname",(session['user_id'],) ).fetchall()
        return render_template("farmdetails.html", crops = crops)

    
@farmsdetails_route.route("/addcrop", methods =["POST"])
@login_required 
def addcrop():
    crop = request.form.get("crop")
    date_planted = request.form.get("date_planted")
    date_harvest = request.form.get("date_harvest")
    stands = request.form.get("stands")
    area = request.form.get("area")
    db=get_db()
    
