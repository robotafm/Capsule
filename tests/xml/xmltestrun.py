import xml.dom.minidom

dom = xml.dom.minidom.parse("test.xml")
dom2 = xml.dom.minidom.parse("test2.xml")

# Do nothing or need?
# dom.normalize()

node1=dom.getElementsByTagName("item")[0]
node2=dom2.getElementsByTagName("item")[0]

print("value="+node1.childNodes[0].nodeValue)
print("attr="+node1.getAttribute("attr4"))

print("value="+node2.childNodes[0].nodeValue)
print("attr="+node2.getAttribute("attr4"))
