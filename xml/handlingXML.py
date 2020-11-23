import xml.etree.ElementTree as ETree

xml1 = ETree.parse('demo.xml')
root = xml1.getroot()
"""
for i in range(len(root)):
    if len(root[i]) == 0:
        if root[i].attrib.keys() == []:
            print(f'Text: {root[i].text}, Tag: {root[i].tag}, Attributes: none')
        else:
            print(f'Text: {root[i].text}, Tag: {root[i].tag}, Attributes: {root[i].attrib}')
    else:
        for j in range(len(root[i])):
            print(f'Text: {root[i][j].text}, Tag: {root[i][j].tag}, Attributes: {root[i][j].attrib}')
"""
def tagValues(tag):
    xml1 = ETree.parse('demo.xml')
    root = xml1.getroot()

    def recursion(elementTree):
        for i in range(len(elementTree)):
            if len(elementTree[i]) == 0:
                if elementTree[i].tag == tag:
                    print(elementTree[i].text)
            else:
                recursion(elementTree[i])
    
    recursion(root)

def documentNodesWithAttribute(attribute):
    xml1 = ETree.parse('demo.xml')
    root = xml1.getroot()
    nodes = 0

    def recursion(elementTree):
        for i in range(len(elementTree)):
            if len(elementTree[i]) == 0:
                if attribute in elementTree[i].attrib.keys():
                   print('test')
            else:
                recursion(elementTree[i])

    recursion(root)

print(documentNodesWithAttribute('fff'))
#tagValues('pc_item')