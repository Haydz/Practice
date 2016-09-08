import xml.etree.ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

print root
print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib


    #childeren are nested

# can find out which element by:
print root[0][1]
#Can get element text via
print root[0][1].text

# identify the number of items in root
#
# print len(root)
for x in range(len(root)):
    print root[x][1].text


for gdppc in root.iter('gdppc'):
    print gdppc.text

    # can modify XML file and stuff
    https: // docs.python.org / 2 / library / xml.etree.elementtree.html