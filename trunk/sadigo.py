#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Diogenes Herminio on 2010-06-24.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from flask import Flask, render_template, session, url_for, request, redirect, flash
from forms import LoginForm, UploadForm

app = Flask(__name__)
app.secret_key = 'bolas'

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/admin', methods=['POST', 'GET']) 
def admin():
    form = UploadForm()
    if request.method == 'POST':
        if form.validate():
            flash('Video upload successfully')
            return redirect(url_for('admin'))
    return render_template('admin.html', form=form.as_widget())

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm()
        if form.validate():
            session['logged_in'] = True
            flash('Logged with success', category='message')
            return redirect(url_for('admin'))
    return render_template('login.html', form=form.as_widget())
    
@app.route('/logout') 
def logout():
    flash('Successful logout', category='message')
    session.pop('logged_in', None)
    return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)