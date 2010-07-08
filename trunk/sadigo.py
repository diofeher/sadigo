#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Diogenes Herminio on 2010-06-24.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.secret_key = 'bolas'

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form.as_widget())
    
@app.route('/logout') 
def logout():
    pass
    
if __name__ == "__main__":
    app.run(debug=True)