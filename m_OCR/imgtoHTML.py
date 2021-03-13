import pytesseract
import cv2
import os
import xml.dom.minidom

image_file = r'C:\Data2\OCR\test_page.png'
alto_xml_file = r'C:\Data2\OCR\text_in_alto.xml'
result_file = r'C:\Data2\OCR\result.html'

def get_text(input_file=image_file, output_file=alto_xml_file):
    """
    Converting img file to text with tesseract library.
    """
    # Tesseract command file in installation directory
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # Load image
    image = cv2.imread(input_file)

    # Run tesseract, returning binary text ALTO xml
    alto_xml = pytesseract.image_to_alto_xml(image, lang='rus+eng') #use

    # Save output xml
    f = open(output_file, "wb")
    f.write(alto_xml)
    f.close()
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
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height



def convert_xml_to_HTML(input_file=alto_xml_file, output_file=result_file):
    """ 
    Convertion function from ALTO xml to HTML page (TODO:pages).
    """


    dom = xml.dom.minidom.parse(input_file)

    page = Page()

    page.width = dom.getElementsByTagName("Page")[0].getAttribute("WIDTH")
    page.height = dom.getElementsByTagName("Page")[0].getAttribute("HEIGHT")

    # Empty new text
    text = ""

    text = add_div_tag(
        text, 
        attribute='width=\"'+page.width+'px\" '+'height=\"'+page.height+'px\"', 
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

        text = add_div_tag(
            text,
            attribute='style=\"position: absolute; top: '+y+'px; left: '+x+'px; font-size: '+height+'px;\"', 
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

def main():
	"""
	Just convertion from default image file to default HTML 
	file (and default ALTO xml file).
	"""
	get_text()
	convert_xml_to_HTML()


if __name__ == '__main__':
	main()
