# Capsule/m_OCR.py
# module for optical character recognition
# use for text convertion to HTML page from imgs
# based on tesseract

# imports:
import xml.dom.minidom
import os
from flask import Flask, render_template, request, Markup, redirect

import Capsule.m_OCR.img_to_text as img_to_text

# constants:
LANG = "../lang/rus.xml"
UPLOAD_FOLDER = r'C:\Data2\uploads'

def clear_upload_folder():
    """Cleaning upload folder"""
    directory = os.listdir(UPLOAD_FOLDER)
    for data in directory:
        os.remove(os.path.join(UPLOAD_FOLDER, data))

# Clear folder
clear_upload_folder()

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
button_prev_page = dom.getElementsByTagName("button_prev_page")[0].childNodes[0].nodeValue
button_next_page = dom.getElementsByTagName("button_next_page")[0].childNodes[0].nodeValue

current_page = 1
current_book = None
current_book_page_count = 0
progress = 0
path = ""
# Flask init:
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# m_OCR web page:
@app.route('/index', methods=['GET', 'POST'])
def index():
    start = request.args.get('start') 
    stop = request.args.get('stop')
    restart = request.args.get('restart')
    global current_book
    global current_book_page_count
    global current_page
    global path
    global progress
    book = current_book
    page = current_page
    page_count = 0
    if request.method == 'POST':
        # Clear folder
        clear_upload_folder()
        files = request.files.getlist('input_file')
        num_of_files = len(files)
        for file in files:
            filename = file.filename
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # Save new file
            file.save(path)
            # Progress bar 10%
            progress = 10
    if(start=="True"):
        directory = os.listdir(app.config['UPLOAD_FOLDER'])
        if(directory!=[]):
            for file in directory:
                path = os.path.join(app.config['UPLOAD_FOLDER'], file)
                # Get book from file
                book = img_to_text.get_book(
                    input_file=path,
                    output_file=path+".xml"
                    )
                current_book = book
                page = 1
                current_page = page
                page_count = book.page_number
                current_book_page_count = page_count
                # Progress bar 100%
                progress = 100
            # Clear folder
            clear_upload_folder()
    return render_template(
        'index.html', 
        m_OCR_name=m_OCR_name, 
        m_OCR_description=m_OCR_description,
        button_start=button_start,
        button_stop=button_stop,
        button_restart=button_restart,
        button_submit=button_submit,
        text_page=Markup(img_to_text.convert_xml_to_HTML(book, page)),
        button_prev_page=button_prev_page,
        button_next_page=button_next_page,
        page=page,
        page_count=current_book_page_count,
        progress = progress
        )

@app.route("/next_page/", methods=['POST'])
def next_page():
    global progress
    global current_page
    global current_book
    progress = 0
    current_page += 1
    if (current_page > current_book.page_number):
        current_page = current_book.page_number
    return redirect('/index')

@app.route("/prev_page/", methods=['POST'])
def prev_page():
    global progress
    global current_page
    progress =0
    current_page -= 1
    if (current_page < 1):
        current_page = 1
    return redirect('/index')

@app.route("/start/", methods=['POST'])
def start():
    return redirect('/index?start=True')

@app.route("/stop/", methods=['POST'])
def stop():
    return redirect('/index?stop=True')

@app.route("/restart/", methods=['POST'])
def restart():
    return redirect('/index?restart=True')