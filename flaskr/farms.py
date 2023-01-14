import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from flaskr.db import get_db
from flaskr.users import login_required

farms_route = Blueprint('farms', __name__)

@farms_route.route('/farms', methods = ["GET", "POST"])
@login_required
def show_farms():
    if request.method =="GET":
        db = get_db()
        farms = db.execute("SELECT * FROM farms WHERE user_id = ?",(session['user_id'],)).fetchall()
        return render_template("farms.html", farms = farms)
 
 
@farms_route.route('/newfarm', methods = ["GET", "POST"])
@login_required
def new_farm():
    if request.method =="GET":
        return render_template("newfarm.html")
    else:
        db=get_db()
        farmname = request.form.get("farmname")
        location = request.form.get("location")
        description = request.form.get("description")
        user_id = session['user_id']
        
        db.execute("INSERT INTO farms (user_id,farmname,location, description) VALUES (?,?,?,?)", (user_id,farmname, location, description))
        db.commit()
        
        return redirect("/farms")
    
    
            
     
        
    
    
