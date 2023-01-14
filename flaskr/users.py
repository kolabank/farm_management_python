import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash,generate_password_hash
from flaskr.db import get_db
from flaskr.__init__ import create_app

user_route = Blueprint('users', __name__)

@user_route.route('/register', methods = ["GET", "POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")
    
    else:
        username= request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        hashed_password = generate_password_hash(password)
        db=get_db()
        error = None
          
        if not email:
            error = 'failure'
            flash("Email is required")  
                      
        elif not username:
            error = 'failure'
            flash("Username is required")
                      
        elif not password:
            error = 'failure'
            flash("Password is required")
                
        if error is None:
            try:
                db.execute("INSERT INTO users (email,username, password) VALUES (?,?,?)", (email,username,hashed_password))
                db.commit()
            except db.IntegrityError:
                error = f"Username {username} is already registered"
            else:
                error ="success"
                flash(f"{username}, you have successfully registered")
                return redirect("/login")
                
               
    return render_template('register.html', error=error)
                        

@user_route.route('/login', methods = ["GET", "POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute("SELECT * FROM users WHERE username = ?",(username,)).fetchone()
        if user is None:
            error = "Incorrect username"
        elif not check_password_hash(user['password'], password):
            error = "Incorrect Password"
            
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect("/farms")
        
        flash(error)
        
    return render_template("login.html")

@user_route.route('/logout', methods = ["GET"])
def logout():
    if request.method =="GET":
        session.clear()
        return redirect('/login')
    
    
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get("user_id") is None:
            return redirect('/login')

        return view(**kwargs)

    return wrapped_view