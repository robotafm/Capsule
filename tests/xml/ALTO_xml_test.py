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
                class_="",
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
            "<div "+class_+">"+
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
    class_='width=\"'+page.width+'\" '+'height=\"'+page.height+'\"', 
    )

lines_of_text = dom.getElementsByTagName("TextLine")

content = ""

line_index = 0
for line in lines_of_text:
    
    line_index += 1
    
    width = line.getAttribute("WIDTH")
    height = line.getAttribute("HEIGHT")
    x = line.getAttribute("VPOS")
    y = line.getAttribute("HPOS")
    
    words = line.getElementsByTagName("String")

    line_text = ""
    for word in words:
        line_text += word.getAttribute("CONTENT")+" "
    content += line_text

    text = add_div_tag(
        text,
        content=content,
        relative_level=line_index,
        div_spacer="\n"
        )
    content = ""



# text = add_div_tag(
#     text, 
#     class_='align=\"left\"', 
#     content='BADABUM!',
#     relative_level=1
#     )

# text = add_div_tag(
#     text, 
#     class_='align=\"right\"', 
#     content='Oh!',
#     relative_level=2
#     )

# text = add_div_tag(
#     text, 
#     class_='align=\"right\"', 
#     content='Egege...',
#     relative_level=3
#     )

print(text)

# node2=dom2.getElementsByTagName("item")[0]
# node3=dom3.getElementsByTagName("warning")[0]

# print("value="+node1.childNodes[0].nodeValue)
# print("attr="+node1.getAttribute("attr4"))

# print("value="+node2.childNodes[0].nodeValue)
# print("attr="+node2.getAttribute("attr4"))

# print("value="+node3.childNodes[0].nodeValue)

# # save output html
# f = open(output_file, "w")
# f.write(result_html)
# f.close()




#list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]
