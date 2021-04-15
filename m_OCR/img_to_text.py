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
import tempfile
import time
import subprocess as sp

import m_BD.BD_lib as BD_lib

djvu_file = r'D:\Data\testdata\djvu\test2_multipage.djvu'
image_file = r'D:\Data\testdata\img\OCR\tests.png'
alto_xml_file = r'D:\Data\testdata\xml\text_in_alto.xml'
result_file = r'D:\Data\testdata\html\result.html'

Ddjvu_cmd = r'C:\"Program Files (x86)"\DjVuLibre\ddjvu.exe -format=tiff -eachpage -skip'


def get_current_server_hash():
    """
    Get sha3_512 hash sum of current server from hostname, 
    ip-adress and platform.
    """
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    platform = sys.platform
    hasher_sha3_512 = hashlib.sha3_512()
    text = (hostname+'|'+ip_address+'|'+platform).encode()
    hasher_sha3_512.update(text)
    return(hasher_sha3_512.hexdigest())

def convert_djvu_to_tiff(input_file, folder):
    """
    Function for convertion .djvu file to .tiff (each page in diffrent file)
    """
    output_file = os.path.join(folder, "page%d.tiff") # %d -> page number 
                                                      # (if -eachpage in Ddjvu_cmd)
    dirpath = r'C:\Program Files (x86)\DjVuLibre'
    filename = r'ddjvu.exe'
    cmd_args = []
    cmd_args.append(os.path.join(dirpath,filename))
    cmd_args.append('-format=tiff')
    cmd_args.append('-eachpage')
    cmd_args.append('-skip')
    cmd_args.append(input_file)
    cmd_args.append(output_file)
    # Run process
    child = sp.Popen(cmd_args)
    # Wait for finish
    child.wait()

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


def convert_djvu_to_xml(input_file=djvu_file):
    """
    Converting djvu to ALTO xml.
    """
    # If book in database       
    hasher_sha3_512 = hashlib.sha3_512()
    file = open(input_file, "rb")
    buf = file.read()
    hasher_sha3_512.update(buf)
    file.close()
    book = BD_lib.get_book_from_database(book_hash=hasher_sha3_512.hexdigest())
    if (book!=None):
        return(book.ALTO_xml)
    else:
        # Create a multi-page ALTO xml document. 
        alto_xml = None
        page_number = 0
        with tempfile.TemporaryDirectory() as temp_folder:
            convert_djvu_to_tiff(input_file, temp_folder)
            filelist = os.listdir(temp_folder)
            for file in filelist:
                path = os.path.join(temp_folder, file)
                alto_xml_page = convert_file_to_xml(path)
                alto_xml = add_page_to_xml(alto_xml, alto_xml_page)
        return (alto_xml)


def convert_file_to_xml(input_file=image_file):
    """
    Converting image files to ALTO xml and
    use convert_djvu_to_xml() and convert_pdf_to_xml().
    """

    # If image file:
    # Windows bitmaps - *.bmp, *.dib
    # JPEG files - *.jpeg, *.jpg, *.jpe
    # JPEG 2000 files - *.jp2
    # Portable Network Graphics - *.png
    # WebP - *.webp
    # Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm
    # Sun rasters - *.sr, *.ras
    # TIFF files - *.tiff, *.tif
    # OpenEXR Image files - *.exr
    # Radiance HDR - *.hdr, *.pic
    valid_image_extensions = [
                             ".bmp", ".dib",
                             ".jpeg", ".jpg", ".jpe",
                             ".jp2", 
                             ".png",
                             ".webp"
                             ".pbm", ".pgm", ".ppm", 
                             ".sr", ".ras", 
                             ".tiff", ".tif",
                             ".exr",
                             ".hdr", ".pic"
                             ]
    extention = os.path.splitext(input_file)[1].lower()
    if extention in valid_image_extensions:
        # Tesseract command file in installation directory
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        # Load image
        image = cv2.imread(input_file)
        # Run tesseract, returning binary text ALTO xml
        alto_xml = pytesseract.image_to_alto_xml(image, lang='rus+eng')
        return(alto_xml)
    elif extention == ".pdf":
        pass # TODO: pdf convertion function
    elif (extention == ".djvu") or (extention == ".djv"):
        alto_xml = convert_djvu_to_xml(input_file)
        return(alto_xml)
    else:
        pass


def get_book(input_file=image_file, output_file=alto_xml_file):
    """
    Get book in ALTO xml from database (if exist) or convertation 
    function (if not).
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
        return(book)
    # If not
    alto_xml = convert_file_to_xml(input_file)
    # # Save output xml to file
    # f = open(output_file, "wb") 
    # f.write(alto_xml)
    # f.close()
    # Save output xml to database
    name = os.path.basename(input_file)
    fullpath = os.path.dirname(input_file)
    ALTO_xml = alto_xml
    book_hash_sha3_512 = hasher_sha3_512.hexdigest()
    server_hash_sha3_512 = get_current_server_hash()
    dom = xml.dom.minidom.parseString(ALTO_xml)
    page = dom.getElementsByTagName("Page").length # Page number
    book = BD_lib.add_book_to_database(
        name=name, 
        fullpath=fullpath, 
        ALTO_xml=ALTO_xml, 
        book_hash_sha3_512=book_hash_sha3_512, 
        server_hash_sha3_512=server_hash_sha3_512,
        page_number=page
        )
    return(book)


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
    def __init__(self, number=0, width=0, height=0, alto_xml=None, HTML=None):
        self.number = number
        self.width = width
        self.height = height
        self.alto_xml = alto_xml
        self.HTML = HTML

def convert_xml_to_HTML(book, page_number=1):
    """ 
    Convertion function from ALTO xml to HTML page.
    """
    if(book == None):
        return(None)
    dom = xml.dom.minidom.parseString(book.ALTO_xml)
    page = Page(number=page_number, alto_xml=dom.getElementsByTagName("Page")[page_number-1])
    page.width = page.alto_xml.getAttribute("WIDTH")
    page.height = page.alto_xml.getAttribute("HEIGHT")
    # Empty new text
    text = ""
    text = add_div_tag(
        text, 
        attribute=('width=\"'+page.width+'px\" '+'height=\"'+page.height+'px\"'+
                   ' style=\"position: absolute;'+
                   'width: '+page.width+'px; height='+page.height+'px;\"'), 
        )


    lines_of_text = page.alto_xml.getElementsByTagName("TextLine")

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
    page.HTML = text
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
        book = None
        # If file is image file
        if((file.find(".xml")<0) and (file.find(".html")<0)):
            book = get_book(
                input_file=os.path.join(folder, file),
                output_file=os.path.join(folder, file+".xml")
                )
            return(convert_xml_to_HTML(book))
    else:
        return(None)



def main():
    """
    Just for testing functions.
    """
    pass


if __name__ == '__main__':
    main()
