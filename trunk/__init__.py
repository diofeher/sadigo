#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Diogenes Herminio on 2010-07-08.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

if __name__ == "__main__":
    from models import db
    db.create_all()