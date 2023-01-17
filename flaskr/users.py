import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash,generate_password_hash
from flaskr.db import get_db
from flaskr.__init__ import create_app

user_route = Blueprint('users', __name__)



@user_route.route('/login', methods = ["GET", "POST"])
def login():
    if request.method =="GET":
        return render_template("login.html")
    
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db()
        error = None
        
        if not username:
            error = 'warning'
            flash("Username is required", error)
            
        elif not password:
            error="warning"
            flash("Password is required", error)
                          
        user = db.execute("SELECT * FROM users WHERE username = ?",(username,)).fetchone()
        
        if user is None:
            error = "warning"
            flash("Incorrect username or password", error)
        elif not check_password_hash(user['password'], password):
            error = "warning"
            flash("Incorrect username or password", error)
            
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect("/farms")
        
               
    return render_template("login.html", error = error)


@user_route.route('/register', methods = ["GET", "POST"])
def register():
    if request.method =="GET":
        return render_template("register.html")
    
    else:
        username= request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        hashed_password = generate_password_hash(password)
        db=get_db()
        error = None
          
        if not email:
            error = 'warning'
            flash("Email is required", error)  
                      
        elif not username:
            error = 'warning'
            flash("Username is required", error)
                      
        elif not password:
            error = 'warning'
            flash("Password is required", error)
                
        if error is None:
            try:
                db.execute("INSERT INTO users (email,username, password) VALUES (?,?,?)", (email,username,hashed_password))
                db.commit()
            except db.IntegrityError:
                error = f"Username {username} is already registered"
                flash(error,"warning")
            else:
                flash(f"{username}, you have successfully registered", "success")
                return redirect("/login")
                
               
    return render_template('register.html')
                        


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