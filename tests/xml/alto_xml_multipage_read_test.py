# imports:
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
import xml.dom.minidom
import m_BD.BD_lib as BD_lib

# Создать БД sqlite:
engine = create_engine(r'sqlite:///C:\Data2\database.db', echo=False) # echo -> печать SQL запросов
metadata = MetaData()
book = BD_lib.get_book_from_database('6552ae8cbd90a1bb05ce1c1667fad6806b34c16d9026168def050720e26525cb7cf30eca132352b437dae95b989509abd0d811e2f467ec8db3a9bdb7fe3cdae4')
dom = xml.dom.minidom.parseString(book.ALTO_xml)
page = dom.getElementsByTagName("Page").length

print(page)
print(book.page_number)