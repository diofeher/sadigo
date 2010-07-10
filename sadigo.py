#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Diogenes Herminio on 2010-06-24.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

import os
import subprocess

from flask import Flask, render_template, session, url_for, request, redirect, flash
from forms import LoginForm, UploadForm
from flaskext.fungiform import ValidationError
from models import Video, db

app = Flask(__name__)
app.secret_key = 'bolas'

@app.route('/')
def index():
    video = Video.query.all()
    return render_template('index.html', videos=video)
  
@app.route('/admin', methods=['POST', 'GET']) 
def admin():
    form = UploadForm()
    validated_data = None
    if request.method == 'POST':
        video = request.files['video']
        fn = video.filename
        name = os.path.splitext(fn)[0]
        fn_new = "%s.flv" % name
        video.save(fn)
        ffmpeg = 'ffmpeg -i %s -y %s' %(fn, fn_new)
        print ffmpeg
        #subprocess.Popen(ffmpeg)
        #subprocess.Popen('rm %s' % fn)
        try:
            video_obj = Video(name, fn_new)
            db.session.add(video_obj)
            db.session.commit()
            flash('Video upload successfully')
        except Exception, e:
            flash('This file already exists')
        return redirect(url_for('admin'))
    else:
        logged_in = session.get('logged_in', '')
        if not logged_in:
            flash('Login please')
            return redirect(url_for('index'))
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
    from database import init_db
    init_db()
    app.run(debug=True)