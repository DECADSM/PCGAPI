import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
    )
from werkzueg.sercurity import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

#Register user
@bp.route('/register', methods=('GET', 'POST'))

def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        dv = get_db()
        error = None
        
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        
        if error is None:
            try:
                db.execute(
                "INSERT INTO user (username, password) VALUES (?, ?)",
                (username, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirection(url_for("auth.login"))
                
        flash(error)
    return render_template('auth/register.html')    
   
#User Login

