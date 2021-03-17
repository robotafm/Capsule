# Capsule/m_BD.py
# Database module with web interface.
# Designed for storing information and settings 
# of all other modules and their automated launch. 
# Based on liteSQL and Flask.

# imports:
import xml.dom.minidom
import os
from flask import Flask, render_template

# constants:
LANG = "../lang/rus.xml"

# XML: load text strings from language file
dom = xml.dom.minidom.parse(LANG)

m_OCR_name = dom.getElementsByTagName("m_BD_name")[0].childNodes[0].nodeValue
    
# Flask init:
app = Flask(__name__)

# m_BD web page:
@app.route('/')
def index():
    return render_template(
        'index.html', 
        m_BD_name=m_BD_name
        )
