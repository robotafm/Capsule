# /robotafm/Capsule/web_int/interface.py
# Main web interface, contains basic
# functions information display

# imports:
from flask import Flask, render_template

# Flask init:
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# NOT WORK
def server_start(port=80):
    """
    Запуск сервера для отображения информации
    port: Номер порта, на котором запускается сервер
    """
    pass #do nothing


# NOT WORK
def server_stop():
    """
    Останавливает запущенный сервер
    """
    pass #do nothing

# NOT WORK
server_start(777)

# Running constantly
# server_stop() 

