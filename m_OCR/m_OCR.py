# Capsule/m_OCR.py
# module for optical character recognition
# use for text convertion to HTML page from imgs
# based on tesseract

# imports:
import xml.dom.minidom
import os
from flask import Flask, render_template, request, Markup

import Capsule.m_OCR.img_to_HTML as img_to_HTML

# constants:
LANG = "../lang/rus.xml"
UPLOAD_FOLDER = r'C:\Data2\uploads'

# Clear folder
directory = os.listdir(UPLOAD_FOLDER)
for data in directory:
    os.remove(os.path.join(UPLOAD_FOLDER, data))

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
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# m_OCR web page:
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files[input_file]
        filename = file.filename
        # Save new file
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return render_template(
        'index.html', 
        m_OCR_name=m_OCR_name, 
        m_OCR_description=m_OCR_description,
        button_start=button_start,
        button_stop=button_stop,
        button_restart=button_restart,
        input_file=input_file,
        button_submit=button_submit,
        text_page=Markup(img_to_HTML.get_HTML(UPLOAD_FOLDER))
        )
