# /robotafm/Capsule/web_int/interface.py
# Main web interface, contains basic
# functions information display

# imports:
import xml.dom.minidom
from flask import Flask, render_template

# constants:
LANG = "../lang/rus.xml"

# XML: load text strings from language file
dom = xml.dom.minidom.parse(LANG)
main_title = dom.getElementsByTagName("main_title")[0].childNodes[0].nodeValue
language = dom.getElementsByTagName("language")[0].childNodes[0].nodeValue
greeting = dom.getElementsByTagName("greeting")[0].childNodes[0].nodeValue
warning = dom.getElementsByTagName("warning")[0].childNodes[0].nodeValue
invitation = dom.getElementsByTagName("invitation")[0].childNodes[0].nodeValue
admin_name = dom.getElementsByTagName("admin_name")[0].childNodes[0].nodeValue
resourse_monitor = dom.getElementsByTagName("resourse_monitor")[0].childNodes[0].nodeValue
database = dom.getElementsByTagName("database")[0].childNodes[0].nodeValue
main_page = dom.getElementsByTagName("main_page")[0].childNodes[0].nodeValue

# Flask init:
app = Flask(__name__)

# Main site page:
@app.route('/')
def index():
    return render_template(
        'index.html', 
        main_title=main_title, 
        admin_name=admin_name, 
        greeting=greeting,
        warning=warning,
        invitation=invitation
        )

# Admin panel:
@app.route('/admin_panel')
def admin_panel():
    return render_template(
        'admin_panel.html', 
        admin_name=admin_name, 
        resourse_monitor=resourse_monitor, 
        database=database,
        main_page=main_page
        )

