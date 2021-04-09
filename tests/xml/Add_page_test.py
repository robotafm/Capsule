import hashlib
import pytesseract
import cv2
import os
import sys
import socket
import xml.dom.minidom
import tempfile
import time
import subprocess as sp


djvu_file = r'D:\Data\testdata\djvu\test2_multipage.djvu'
image_file = r'D:\Data\testdata\img\OCR\tests.png'
alto_xml_file = r'D:\Data\testdata\xml\text_in_alto.xml'
result_file = r'D:\Data\testdata\html\result.html'


def add_page_to_xml(alto_xml, alto_xml_page, page_number=0):
    """
    Add new page to end of alto_xml or replace old page.
    """    
    # If book empty
    if (alto_xml == None):
        page_dom = xml.dom.minidom.parseString(alto_xml_page)
        page_dom.getElementsByTagName("Page")[0].setAttribute("ID", 'page_1')
        alto_xml_page = page_dom.toxml(encoding="utf-8")
        return(alto_xml_page)
    # If not
    book_dom = xml.dom.minidom.parseString(alto_xml)
    page_dom = xml.dom.minidom.parseString(alto_xml_page)
    page = page_dom.getElementsByTagName("Page")[0]
    if(page_number==0):
        # Find last page
        page_number = book_dom.getElementsByTagName("Page").length
        # and add page to end
        book_dom.getElementsByTagName("Layout")[0].appendChild(page)
        page.setAttribute("ID", 'page_%d' % (page_number+1))
    # If new page is not last page
    else:
        old_page = book_dom.getElementsByTagName("Page")[page_number-1]
        book_dom.getElementsByTagName("Layout")[0].replaceChild(page, old_page)
        page.setAttribute("ID", 'page_%d' % page_number)
    return(book_dom.toxml(encoding="utf-8"))

def main():
    file_1 = open(os.path.join(r'D:\Data\testdata\xml', 'text_in_alto.xml'), 'rb')
    file_2 = open(os.path.join(r'D:\Data\testdata\xml', 'next_page.xml'), 'rb')
    result_1 = add_page_to_xml(None, file_1.read().decode("utf-8"))
    result_2 = add_page_to_xml(result_1, file_2.read().decode("utf-8"))
    file_2.close()
    file_2 = open(os.path.join(r'D:\Data\testdata\xml', 'next_page.xml'), 'rb')
    result_3 = add_page_to_xml(result_2, file_2.read().decode("utf-8"))
    file_1.close()
    file_2.close()
    file_3 = open(os.path.join(r'D:\Data\tmp', 'text_in_alto.xml'), 'wb')
    file_3.write(result_3)
    file_3.close()

    file_2 = open(os.path.join(r'D:\Data\testdata\xml', 'next_page.xml'), 'rb')
    file_3 = open(os.path.join(r'D:\Data\tmp', 'text_in_alto.xml'), 'rb')
    result = add_page_to_xml(file_3.read().decode("utf-8"), file_2.read().decode("utf-8"), page_number=1)
    file_3.close()
    file_2.close()

    with open(os.path.join(r'D:\Data\tmp', 'text_in_alto.xml'), 'wb') as file_3:
        file_3.write(result)

if __name__ == '__main__':
    main()