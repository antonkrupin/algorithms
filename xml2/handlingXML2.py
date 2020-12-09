import xml.etree.ElementTree as ETree

def tagNodesList(rootNode, tag, fileName):
    try:
        xml = ETree.parse(fileName)
        root = xml.getroot()
        nodesList = []

        if root.tag == rootNode:
            for item in root.iter():
                if tag == item.tag:
                    nodesList.append(item.tag)
            return [nodesList, 1]
        else:
            return [nodesList, -1]
    except Exception:
        return ['no file', -1]


def findParent(node, fileName):
    try:
        xml = ETree.parse(fileName)
        root = xml.getroot()
    
        if node == root.tag:
            return [root.tag, 1]

        nodesList = []
        for item in root:
            nodesList.append(item.tag)

        if node in nodesList:
            return [root, 1]
        else:
            for item in root:
                bc = item.findall(node)
                if bc != []:
                    return [item, 1]

        return [node, -1]
    except Exception:
        return ['no file', -1]

    
def deleteNodes(tag, fileName):
    try:
        xml = ETree.parse(fileName)
        root = xml.getroot()

        for item in root:
            if len(item) == 0:
                nodeForDelete = root.find(tag)
                if nodeForDelete != None:
                    root.remove(nodeForDelete)
            else:
                for i in range(len(item)):
                    nodeForDelete = item.find(tag)
                    if nodeForDelete != None:
                        item.remove(nodeForDelete)
                        
        fileName = 'new_'+fileName
        xml.write(fileName)
        return 1
    except Exception:
        return -1


print(deleteNodes('test1', 'demo1.xml'))
#print(findParent('pc','demo.xml'))
#print(tagNodesList('data','languages', 'fileWithDeletedNode.xml'))