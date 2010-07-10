#!/usr/bin/env python
# encoding: utf-8
"""
models.py

Created by Diogenes Herminio on 2010-06-24.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from sqlalchemy import Column, Integer, String
from database import db_session, Base
from flask import Flask
from flaskext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
db = SQLAlchemy(app)

class Video(Base):
    query = db_session.query_property()
    
    __tablename__ = 'videos'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    filepath = Column(String(200), unique=True)
    
    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath
        
    def __repr__(self):
        return 'Cool Video %s' % (self.name,)