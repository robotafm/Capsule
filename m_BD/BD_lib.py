# Capsule/m_BD/BD_lib.py
# A library with functions for accessing to
# the database and functions for controlling 
# other modules (start, stop, and so on). 
# Based on liteSQL.

# imports:
import sqlite3 as sl
import pandas as pd


def start_module(name):
    id = -1
    return(id)

def stop_module(id):
    return(True)

def pause_module(id):
    return(True)

def is_module_run(id):
    return(True)

def is_module_pause(id):
    return(True)

def get_module_status(id):
    status = -1
    return (status)

def add_to_database(data):
    link = None
    return(link)

def get_from_database(link):
    data = None
    return(data)

