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

        for i in range(len(root)):
            if len(root[i]) == 0:
                print(root[i].text)
            else:
                for j in range(len(root[i])):
                    print(root[i][j].text)

        return [tag, 1]
    except Exception:
        return [tag, -1]

def documentNodesWithAttribute(attribute, file):
    try:
        xml1 = ETree.parse(file)
        root = xml1.getroot()
        nodes = 0
        for i in range(len(root)):
            if len(root[i]) == 0:
                if attribute in root[i].attrib.keys():
                    nodes += 1
            else:
                for j in range(len(root[i])):
                    if attribute in root[i][j].attrib.keys():
                        nodes += 1

        return [nodes, 1]
    except Exception:
        return [0, -1]
