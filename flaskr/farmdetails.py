import functools
import sqlite3
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flaskr.db import get_db
from flaskr.users import login_required

farmsdetails_route = Blueprint('farmdetails', __name__)

#Route to display list of crops in the select section. Crops taken from crops database
@farmsdetails_route.route("/farmdetails/<id>", methods =["GET", "POST"])
@login_required
def farmdetail(id):
    if request.method == "GET":
        db = get_db()
        session['farm_id'] = id
    
        plants = db.execute("SELECT * FROM plantdetails WHERE farm_id = ?", id)
        
        #Extract to list crop that will be in the dropdown list to select a new crop
        crops = db.execute("SELECT cropname, cropbreed FROM crops WHERE user_id = ? ORDER BY cropname",(session['user_id'],) ).fetchall()
        
        return render_template("farmdetails.html", crops = crops, plants = plants)

    
@farmsdetails_route.route("/addcrop", methods =["POST"])
@login_required 
def addcrop():
    #Get inputs from all forms
    crop = request.form.get("crop")
    breed = request.form.get("breed")
    date_planted = request.form.get("date_planted")
    date_harvest = request.form.get("date_harvest")
    stands = request.form.get("stands")
    area = request.form.get("area")
    db=get_db()
    
    # This is to get the crop id to be inserted to the plantdetails table
    selected_crop = db.execute("SELECT*FROM crops WHERE cropname = ? AND cropbreed = ?", (crop, breed)).fetchone()
    
    if selected_crop is None:
        
        flash("You have chosen the wrong breed")
    else:
        crop_id = selected_crop['id']
                       
        # Extract the farm that the planting corresponds to
    
        db.execute("INSERT INTO plantdetails (crop, farm_id, crop_id, breed, date_planted, date_harvest, stands, area) VALUES (?,?,?,?,?,?,?,?)", (crop, session['farm_id'], crop_id, breed, date_planted, date_harvest, stands,area))
        db.commit()
    
    return redirect(url_for('farmdetails.farmdetail', id = session['farm_id']))
