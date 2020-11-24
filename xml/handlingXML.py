import xml.etree.ElementTree as ETree

def printNodesValues():
    try:
        xml1 = ETree.parse('demo.xml')
        root = xml1.getroot()

        for i in range(len(root)):
            if len(root[i]) == 0:
                if root[i].attrib.keys() == []:
                    print(f'Text: {root[i].text}, Tag: {root[i].tag}, Attributes: none')
                else:
                    print(f'Text: {root[i].text}, Tag: {root[i].tag}, Attributes: {root[i].attrib}')
            else:
                for j in range(len(root[i])):
                    print(f'Text: {root[i][j].text}, Tag: {root[i][j].tag}, Attributes: {root[i][j].attrib}')
        return 1
    except Exception:
        return -1


def tagValues(tag, file):
    try:
        xml1 = ETree.parse(file)
        root = xml1.getroot()
        recursionTagValues(root,tag)
        return [tag, 1]
    except Exception:
        return [tag, -1]
    
def recursionTagValues(elementTree, tag):
    for i in range(len(elementTree)):
        if len(elementTree[i]) == 0:
            if elementTree[i].tag == tag:
                print(elementTree[i].text)
        else:
            recursionTagValues(elementTree[i], tag)


def documentNodesWithAttribute(attribute, file):
    try:
        xml1 = ETree.parse(file)
        root = xml1.getroot()
        nodes = []
        return [recursionDocumentNodes(root,attribute,nodes), 1]
    except Exception:
        return [0, -1]

def recursionDocumentNodes(elementTree,attribute,nodes):
    for i in range(len(elementTree)):
        if len(elementTree[i]) == 0:
            if attribute in elementTree[i].attrib.keys():
                nodes.append(1)
        else:
            recursionDocumentNodes(elementTree[i],attribute,nodes)
    return sum(nodes)
