# Capsule/m_BD/BD_lib.py
# A library with functions for accessing to
# the database and functions for controlling 
# other modules (start, stop, and so on). 
# Based on liteSQL.

# imports:
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

# Создать БД sqlite в оперативной памяти:
engine = create_engine(r'sqlite:///C:\Data2\database.db', echo=False) # echo -> печать SQL запросов
metadata = MetaData()

books_table = Table(
    'books', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullpath', String),
    Column('ALTO_xml', String),
    Column('book_hash_sha3_512', String),
    Column('server_hash_sha3_512', String) # Instead of the server name.
    )


class Book(object):
    def __init__(
                self, 
                name, 
                fullpath, 
                ALTO_xml, 
                book_hash_sha3_512, 
                server_hash_sha3_512
                ):
        self.name = name
        self.fullpath = fullpath
        self.ALTO_xml = ALTO_xml
        self.book_hash_sha3_512 = book_hash_sha3_512
        self.server_hash_sha3_512 = server_hash_sha3_512

    def __repr__(self):
        return "<Book('%s','%s', '%s', '%s', '%s')>" % (
            self.name, 
            self.fullpath, 
            self.ALTO_xml, 
            self.hash_sha3_512, 
            self.server_hash_sha3_512
            )


servers_table = Table(
    'servers', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('server_name', String),
    Column('server_os', String),
    Column('server_IPv4_adress', String),
    Column('server_MAC_adress', String),
    Column('server_CPU', String),
    Column('server_RAM_size', String),
    Column('server_hash_sha3_512', String)
    )


class Server(object):
    def __init__(
                 self, 
                 server_name, 
                 server_os, 
                 server_IPv4_adress, 
                 server_MAC_adress, 
                 server_CPU, 
                 server_RAM_size, 
                 server_hash_sha3_512
                 ):
        self.server_name = server_name
        self.server_os = server_os
        self.server_IPv4_adress = server_IPv4_adress
        self.server_MAC_adress = server_MAC_adress
        self.server_CPU = server_CPU
        self.server_RAM_size = server_RAM_size
        self.server_hash_sha3_512 = server_hash_sha3_512

    def __repr__(self):
        return "<Server('%s','%s', '%s', '%s', '%s', '%s', '%s')>" % (
            self.server_name,
            self.server_os,
            self.server_IPv4,
            self.server_MAC,
            self.server_CPU,
            self.server_RAM,
            self.server_hash_sha3_512
            )

metadata.create_all(engine)

mapper(Book, books_table)
mapper(Server, servers_table)

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

def add_book_to_database(
                         name,
                         fullpath, 
                         ALTO_xml, 
                         book_hash_sha3_512, 
                         server_hash_sha3_512,
                         engine=engine
                         ):
    Session = sessionmaker(bind=engine)
    session = Session()

    query = (session.query(Book.book_hash_sha3_512).filter(
        Book.book_hash_sha3_512==book_hash_sha3_512)
        )
    if (query!=None):
        #TODO: If book not exist, add new book
        pass
    # Adding one entry:
    book = Book(
                name, 
                fullpath, 
                ALTO_xml, 
                book_hash_sha3_512, 
                server_hash_sha3_512
                )
    session.add(book)
    # Saving all changes in the database: 
    session.commit()
    return(book)

# def get_book_from_database(engine=engine):
#     book = None
#     return(book)

# def add_server_to_database():
#     pass

# def get_server_from_database():
#     pass

