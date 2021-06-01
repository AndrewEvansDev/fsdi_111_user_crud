#!/usr/bin/env python3
"""module init file"""

from flask import Flask

app = Flask(__name__) # Dunder variable or magic variable

from app import routes