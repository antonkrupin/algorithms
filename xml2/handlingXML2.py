import xml.etree.ElementTree as ETree

xml = ETree.parse('demo.xml')
root = xml.getroot()

nodes = []

for item in root.iter():
    if 'name' in item.attrib.keys():
        nodes.append(item.tag)

#print(nodes)


def tagNodesList(rootNode, tag):
    xml = ETree.parse('demo.xml')
    root = xml.getroot()
    nodesList = []

    if root.tag == rootNode:
        for item in root.iter():
            if tag == item.tag:
                nodesList.append(item.tag)
        return [nodesList, 1]
    else:
        return [nodesList, -1]

def findParent(node):
    xml = ETree.parse('demo.xml')
    root = xml.getroot()

    if node == root.tag:
        return [root.tag, 1]
    
    nodesList = []
    for item in root:
        nodesList.append(item.tag)

    if node in nodesList:
        return [root.tag, 1]
    else:
        for item in nodesList:
            parentNode = root.find(item)
            if parentNode.findall(node) != []:
                return [item, 1]
        
        return ['none', -1]

print(findParent('test1'))
#print(tagNodesList('data', 'pc_item'))
