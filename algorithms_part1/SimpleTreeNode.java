import java.util.*;

public class SimpleTreeNode<T>
{
    public T NodeValue; // значение в узле
    public SimpleTreeNode<T> Parent; // родитель или null для корня
    public List<SimpleTreeNode<T>> Children; // список дочерних узлов или null

    public SimpleTreeNode(T val, SimpleTreeNode<T> parent)
    {
        NodeValue = val;
        Parent = parent;
        Children = null;
    }
}

class SimpleTree<T>
{
    public SimpleTreeNode<T> Root; // корень, может быть null

    public SimpleTree(SimpleTreeNode<T> root)
    {
        Root = root;
    }

    public void AddChild(SimpleTreeNode<T> ParentNode, SimpleTreeNode<T> NewChild)
    {
        if (ParentNode == null) return;

        if (ParentNode.Children == null) {
            ParentNode.Children = new ArrayList<>();
        }

        ParentNode.Children.add(NewChild);
        NewChild.Parent = ParentNode;
    }

    public void DeleteNode(SimpleTreeNode<T> NodeToDelete)
    {
        if (NodeToDelete == null) return;

        if (NodeToDelete == Root) {
            Root = null;
            return;
        }

        SimpleTreeNode<T> parent = NodeToDelete.Parent;
        if (parent != null && parent.Children != null) {
            parent.Children.remove(NodeToDelete);

            if (parent.Children.isEmpty()) {
                parent.Children = null;
            }
        }

        NodeToDelete.Parent = null;
        NodeToDelete.Children = null;
    }

    public List<SimpleTreeNode<T>> GetAllNodes()
    {
        List<SimpleTreeNode<T>> allNodesList = new ArrayList<>();
        if (Root == null) return allNodesList;

        LinkedList<SimpleTreeNode<T>> nodesList = new LinkedList<>();

        nodesList.push(Root);

        while (!nodesList.isEmpty()) {
            SimpleTreeNode<T> node = nodesList.pop();
            allNodesList.add(node);

            CheckAndPushChildren(nodesList, node);
        }

        return allNodesList;
    }

    public List<SimpleTreeNode<T>> FindNodesByValue(T val)
    {
        List<SimpleTreeNode<T>> findedNodesList = new ArrayList<>();

        if (Root == null) return findedNodesList;

        LinkedList<SimpleTreeNode<T>> nodesList = new LinkedList<>();

        nodesList.push(Root);

        while(!nodesList.isEmpty()) {
            SimpleTreeNode<T> node = nodesList.pop();
            if (node.NodeValue == val) {
                findedNodesList.add(node);
            }

            CheckAndPushChildren(nodesList, node);
        }

        return findedNodesList;
    }

    public void MoveNode(SimpleTreeNode<T> OriginalNode, SimpleTreeNode<T> NewParent)
    {
        if (OriginalNode == null || NewParent == null) return;
        if (OriginalNode == Root) return;
        if (OriginalNode == NewParent) return;

        if (CheckNode(NewParent, OriginalNode)) return;

        SimpleTreeNode<T> oldParentNode = OriginalNode.Parent;
        if (oldParentNode != null && oldParentNode.Children != null) {
            oldParentNode.Children.remove(OriginalNode);

            if (oldParentNode.Children.isEmpty()) {
                oldParentNode.Children = null;
            }
        }

        AddChild(NewParent, OriginalNode);
    }

    public int Count()
    {
        if (Root == null) return 0;

        int counter = 0;
        LinkedList<SimpleTreeNode<T>> nodesList = new LinkedList<>();
        nodesList.push(Root);

        while (!nodesList.isEmpty()) {
            SimpleTreeNode<T> node = nodesList.pop();
            counter = counter + 1;

            if (node.Children != null) {
                for (SimpleTreeNode<T> childNode : node.Children) {
                    nodesList.push(childNode);
                }
            }
        }
        return counter;
    }

    public int LeafCount()
    {
        if (Root == null) return 0;

        int counter = 0;

        LinkedList<SimpleTreeNode<T>> nodesList = new LinkedList<>();
        nodesList.push(Root);

        while (!nodesList.isEmpty()) {
            SimpleTreeNode<T> node = nodesList.pop();

            if (node.Children == null || node.Children.isEmpty()) {
                counter = counter + 1;
            } else {
                for (SimpleTreeNode<T> childNode : node.Children) {
                    nodesList.push(childNode);
                }
            }
        }
        return counter;
    }

    void CheckAndPushChildren(LinkedList<SimpleTreeNode<T>> nodesList, SimpleTreeNode<T> node) {
        if (node.Children != null) {
            for (int i = node.Children.size() - 1; i >= 0; i--) {
                nodesList.push(node.Children.get(i));
            }
        }
    }

    boolean CheckNode(SimpleTreeNode<T> node, SimpleTreeNode<T> parentNode) {
        SimpleTreeNode<T> currentNode = node;
        while (currentNode != null) {
            if (currentNode == parentNode) return true;
            currentNode = currentNode.Parent;
        }
        return false;
    }
}
