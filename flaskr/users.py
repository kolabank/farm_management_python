import functools
from flask import(Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash,generate_password_hash
from flaskr.db import get_db

userRoute = Blueprint('userRoute', __name__)

@userRoute('/register', methods = ['GET', 'POST'])
def register():
    if request.method =="GET":
        return render_template("register.html")