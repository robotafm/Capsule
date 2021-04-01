# Capsule/img_to_text.py
# Library for optical character recognition
# use for convertion pages from images to ALTO XML 
# and from ALTO XML to HTML. 
# Based on pytesseract.

import hashlib
import pytesseract
import cv2
import os
import sys
import socket
import xml.dom.minidom

import Capsule.m_BD.BD_lib as BD_lib

image_file = r'D:\Data\testdata\img\OCR\tests.png'
alto_xml_file = r'D:\Data\testdata\xml\text_in_alto.xml'
result_file = r'D:\Data\testdata\html\result.html'


def get_current_server_hash():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    platform = sys.platform
    hasher_sha3_512 = hashlib.sha3_512()
    text = (hostname+'|'+ip_address+'|'+platform).encode()
    hasher_sha3_512.update(text)
    return(hasher_sha3_512.hexdigest())


def get_xml(input_file=image_file, output_file=alto_xml_file):
    """
    Converting img file to ALTO xml with tesseract library.
    Save result ALTO xml to file and database
    """
    hasher_sha3_512 = hashlib.sha3_512()
    file = open(input_file, "rb")
    buf = file.read()
    hasher_sha3_512.update(buf)
    file.close()
    # If book in database
    book = BD_lib.get_book_from_database(book_hash=hasher_sha3_512.hexdigest())
    if (book!=None):
        # Save output xml to file
        f = open(output_file, "wb")
        f.write(book.ALTO_xml)
        f.close()
        return(book.ALTO_xml)
    # Tesseract command file in installation directory
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Load image
    image = cv2.imread(input_file)
    # Run tesseract, returning binary text ALTO xml
    alto_xml = pytesseract.image_to_alto_xml(image, lang='rus+eng') #use
    # Save output xml to file
    f = open(output_file, "wb")
    f.write(alto_xml)
    f.close()
    # Save output xml to database
    name = os.path.basename(input_file)
    fullpath = os.path.dirname(input_file)
    ALTO_xml = alto_xml
    book_hash_sha3_512 = hasher_sha3_512.hexdigest()
    server_hash_sha3_512 = get_current_server_hash()
    book = BD_lib.add_book_to_database(
        name=name, 
        fullpath=fullpath, 
        ALTO_xml=ALTO_xml, 
        book_hash_sha3_512=book_hash_sha3_512, 
        server_hash_sha3_512=server_hash_sha3_512
        )
    return(alto_xml)


def find_all(a_str, sub):
    """ 
    Find all occurrences of a substring in a string.
    NOTE: I don't understend how it work....
    """
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def add_div_tag(
                text="",
                attribute="",
                content="",
                relative_level=0,
                div_spacer=""
                ):
    """ 
    Add new div tag with content and attributes 
    (width, heght, style etc.) to HTML code.
    """
    if(relative_level!=0):
        indexes = list(find_all(text,'</div>'))
        relative_level -= 1 # Array element offset 
    else:
        indexes = [0]
    text = (text[0:indexes[relative_level]]+
            "<div "+attribute+">"+
            content+
            "</div>"+
            div_spacer+
            text[indexes[relative_level]:])
    return(text)


class Page():
    def __init__(self, number=0, width=0, height=0, alto_xml=None):
        self.number = number
        self.width = width
        self.height = height
        self.alto_xml = alto_xml

def convert_xml_to_HTML(input_file=alto_xml_file, output_file=result_file, page_number=1):
    """ 
    Convertion function from ALTO xml to HTML page (TODO:pages).
    """
    dom = xml.dom.minidom.parse(input_file)
    page = Page(number=page_number)
    page.width = dom.getElementsByTagName("Page")[page.number-1].getAttribute("WIDTH")
    page.height = dom.getElementsByTagName("Page")[page.number-1].getAttribute("HEIGHT")
    # Empty new text
    text = ""
    text = add_div_tag(
        text, 
        attribute=('width=\"'+page.width+'px\" '+'height=\"'+page.height+'px\"'+
                   ' style=\"position: absolute;'+
                   'width: '+page.width+'px; height='+page.height+'px;\"'), 
        )

    lines_of_text = dom.getElementsByTagName("TextLine")

    content = ""

    line_index = 0
    for line in lines_of_text:
        
        line_index += 1
        
        width = line.getAttribute("WIDTH")
        height = line.getAttribute("HEIGHT")
        y = line.getAttribute("VPOS")
        x = line.getAttribute("HPOS")
        
        words = line.getElementsByTagName("String")

        line_text = ""
        for word in words:
            line_text += word.getAttribute("CONTENT")+" "
        content += line_text

        string = content

        text = add_div_tag(
            text,
            attribute=('style=\"position: absolute; top: '+y+'px;'+
                       ' left: '+x+'px; font-size: '+height+'px;\"'), 
            content=content,
            relative_level=line_index,
            div_spacer="\n"
            )
        content = ""

    # save output html
    f = open(output_file, "w")
    f.write(text)
    f.close()
    return(text)


def get_HTML(folder):
    """
    Convertion from images to HTML text.
    folder: directory with image files to convertion.
    Return HTML text in UTF-8.
    """
    directory = os.listdir(folder)
    if(directory!=[]):
        file = directory[0]
        # If file is image file
        if((file.find(".xml")<0) and (file.find(".html")<0)):
            get_xml(
                input_file=os.path.join(folder, file),
                output_file=os.path.join(folder, file+".xml")
            )
            return(
                convert_xml_to_HTML(
                    input_file=os.path.join(folder, file+".xml"), 
                    output_file=os.path.join(folder, file+".html")
                )
            )
    else:
        return(None)



def main():
    """
    Just convertion from default image file to default HTML 
    file (and default ALTO xml file).
    """
    get_xml()
    convert_xml_to_HTML()


if __name__ == '__main__':
    main()
