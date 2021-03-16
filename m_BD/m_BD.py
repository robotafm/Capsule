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

m_OCR_name = dom.getElementsByTagName("m_OCR_name")[0].childNodes[0].nodeValue
m_OCR_description = dom.getElementsByTagName("m_OCR_description")[0].childNodes[0].nodeValue
status_OK = dom.getElementsByTagName("status_OK")[0].childNodes[0].nodeValue
status_UP = dom.getElementsByTagName("status_UP")[0].childNodes[0].nodeValue
status_work = dom.getElementsByTagName("status_work")[0].childNodes[0].nodeValue
status_error = dom.getElementsByTagName("status_error")[0].childNodes[0].nodeValue
button_start = dom.getElementsByTagName("button_start")[0].childNodes[0].nodeValue
button_stop = dom.getElementsByTagName("button_stop")[0].childNodes[0].nodeValue
button_restart = dom.getElementsByTagName("button_restart")[0].childNodes[0].nodeValue
button_submit = dom.getElementsByTagName("button_submit")[0].childNodes[0].nodeValue
input_file="input_file"
    
# Flask init:
app = Flask(__name__)

# m_BD web page:
@app.route('/')
def index():
    return render_template(
        'index.html', 
        m_OCR_name=m_OCR_name, 
        m_OCR_description=m_OCR_description,
        button_start=button_start,
        button_stop=button_stop,
        button_restart=button_restart,
        input_file=input_file,
        button_submit=button_submit,
        text_page=Markup(imgtoHTML.get_HTML(UPLOAD_FOLDER))
        )
