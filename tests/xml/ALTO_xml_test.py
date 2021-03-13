import xml.dom.minidom

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

    if(relative_level!=0):
        indexes = list(find_all(text,'</div>'))
        relative_level -= 1
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


input_file = r'C:\Data2\OCR\alto.xml'
output_file = r'C:\Data2\OCR\result_from_alto_xml.html'

dom = xml.dom.minidom.parse(input_file)

# Do nothing or need?
# dom.normalize()

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


#    font-family: Verdana, Arial, Helvetica, sans-serif; 
#    font-size: 11pt; /* Размер шрифта в пунктах */ 

#list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]
