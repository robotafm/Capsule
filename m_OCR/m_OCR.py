# Capsule/m_OCR.py
# module for optical character recognition
# use for text convertion to HTML page from imgs
# based on tesseract

# imports:
import xml.dom.minidom
from flask import Flask, render_template

# constants:
LANG = "../lang/rus.xml"

# FIX IT:
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

# Flask init:
app = Flask(__name__)

# m_OCR web page:
@app.route('/')
def index():
    return render_template(
        'index.html', 
        m_OCR_name=m_OCR_name, 
        m_OCR_description=m_OCR_description
        )
