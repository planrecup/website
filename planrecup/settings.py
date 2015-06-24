'''
Created on 12 janv. 2014

@author: rux
'''
import os

if os.environ['DJANGO_ENV'] == 'production':
    from planrecup.conf.prod import *
else:
    from planrecup.conf.dev import *

# Just a pointer to the main config module
SECRET_KEY = "KHFUBYFGJHGILU?MHLGHKUH8KJGBUF5 466778"
