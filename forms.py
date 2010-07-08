#!/usr/bin/env python
# encoding: utf-8
"""
forms.py

Created by Diogenes Herminio on 2010-07-08.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from flask import Flask
from flaskext.fungiform import Form, TextField, ValidationError

app = Flask(__name__)
app.secret_key = 'bolas'

class LoginForm(Form):
    login = TextField(required=True)
    password = TextField(required=True)
    
    def context_validate(self, data):
        if data['login'] == 'admin':
            if data['password'] != 'admin':
                raise ValidationError(u'Password incorrect')
        else:
            raise ValidationError(u'Unknown user')