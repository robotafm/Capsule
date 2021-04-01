import xml.dom.minidom

input_file = r'D:\Data\testdata\xml\two_pages_in_alto.xml'
output_file = r'C:\Data2\OCR\result_from_alto_xml.html'

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
    def __init__(self, number=0, width=0, height=0, alto_xml=None):
        self.number = number
        self.width = width
        self.height = height
        self.alto_xml = alto_xml

def add_page_to_alto_xml(input_file=input_file):
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse(input_file);

    # print out the document node and the name of the first child tag
    print (doc.nodeName)
    print (doc.firstChild.tagName)
    # get a list of XML tags from the document and print each one
    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))

    # create a new XML tag and add it into the document
    newexpertise = doc.createElement("expertise")
    newexpertise.setAttribute("name", "BigData")
    doc.firstChild.appendChild(newexpertise)
    print (" ")

    expertise = doc.getElementsByTagName("expertise")
    print ("%d expertise:" % expertise.length)
    for skill in expertise:
        print (skill.getAttribute("name"))

    #TODO: get page xml text from file
    print(doc.getElementsByTagName("Page"))



# dom = xml.dom.minidom.parse(input_file)
# page_number = 1
# page = Page(
#     number=page_number, 
#     alto_xml=dom.getElementsByTagName("Page")[page_number-1]
#     )
# print ("page.alto_xml=", page.alto_xml)
add_page_to_alto_xml()



# page.width = dom.getElementsByTagName("Page")[0].getAttribute("WIDTH")
# page.height = dom.getElementsByTagName("Page")[0].getAttribute("HEIGHT")

# # Empty new text
# text = ""

# text = add_div_tag(
#     text, 
#     attribute='width=\"'+page.width+'px\" '+'height=\"'+page.height+'px\"', 
#     )

# lines_of_text = dom.getElementsByTagName("TextLine")

# content = ""

# line_index = 0
# for line in lines_of_text:
    
#     line_index += 1
    
#     width = line.getAttribute("WIDTH")
#     height = line.getAttribute("HEIGHT")
#     y = line.getAttribute("VPOS")
#     x = line.getAttribute("HPOS")
    
#     words = line.getElementsByTagName("String")

#     line_text = ""
#     for word in words:
#         line_text += word.getAttribute("CONTENT")+" "
#     content += line_text

#     text = add_div_tag(
#         text,
#         attribute='style=\"position: absolute; top: '+y+'px; left: '+x+'px; font-size: '+height+'px;\"', 
#         content=content,
#         relative_level=line_index,
#         div_spacer="\n"
#         )
#     content = ""

# # save output html
# f = open(output_file, "w")
# f.write(text)
# f.close()


#    font-family: Verdana, Arial, Helvetica, sans-serif; 
#    font-size: 11pt; /* Размер шрифта в пунктах */ 

#list(find_all('spam spam spam spam', 'spam')) # [0, 5, 10, 15]
