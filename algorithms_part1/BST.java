class BSTNode<T>
{
    public int NodeKey; // ключ узла
    public T NodeValue; // значение в узле
    public BSTNode<T> Parent; // родитель или null для корня
    public BSTNode<T> LeftChild; // левый потомок
    public BSTNode<T> RightChild; // правый потомок	

    public BSTNode(int key, T val, BSTNode<T> parent)
    {
        NodeKey = key;
        NodeValue = val;
        Parent = parent;
        LeftChild = null;
        RightChild = null;
    }
}

// промежуточный результат поиска
class BSTFind<T>
{
    // null если в дереве вообще нету узлов
    public BSTNode<T> Node;

    // true если узел найден
    public boolean NodeHasKey;

    // true, если родительскому узлу надо добавить новый левым
    public boolean ToLeft;

    public BSTFind() { Node = null; }
}

class BST<T>
{
    BSTNode<T> Root; // корень дерева, или null

    public BST(BSTNode<T> node)
    {
        Root = node;
    }

    public BSTFind<T> FindNodeByKey(int key)
    {
        BSTFind<T> findedNode = new BSTFind<>();

        if (Root == null) {
            return findedNode;
        }

        BSTNode<T> currentNode = Root;

        while (true) {
            if (currentNode.NodeKey == key) {
                findedNode.Node = currentNode;
                findedNode.NodeHasKey = true;
                findedNode.ToLeft = true;
                return findedNode;
            }

            if (key < currentNode.NodeKey) {
                if (currentNode.LeftChild == null) {
                    findedNode.Node = currentNode;
                    findedNode.NodeHasKey = false;
                    findedNode.ToLeft = true;
                    return findedNode;
                }
                currentNode = currentNode.LeftChild;
            } else {
                if (currentNode.RightChild == null) {
                    findedNode.Node = currentNode;
                    findedNode.NodeHasKey = false;
                    findedNode.ToLeft = false;
                    return findedNode;
                }

                currentNode = currentNode.RightChild;
            }
        }
    }

    public boolean AddKeyValue(int key, T val)
    {
        if (Root == null) {
            Root = new BSTNode<T>(key, val, null);
            return true;
        }

        BSTFind<T> findedNode = FindNodeByKey(key);

        if (findedNode.NodeHasKey) {
            return false;
        }

        BSTNode<T> newNode = new BSTNode<T>(key, val, findedNode.Node);

        if (findedNode.ToLeft) {
            findedNode.Node.LeftChild = newNode;
        } else {
            findedNode.Node.RightChild = newNode;
        }

        return true;
    }

    public BSTNode<T> FinMinMax(BSTNode<T> FromNode, boolean FindMax)
    {
        if (FromNode == null) {
            return null;
        }

        BSTNode<T> currentNode = FromNode;

        if (FindMax) {
            while (currentNode.RightChild != null) {
                currentNode = currentNode.RightChild;
            }
        } else {
            while (currentNode.LeftChild != null) {
                currentNode = currentNode.LeftChild;
            }
        }

        return currentNode;
    }

    public boolean DeleteNodeByKey(int key)
    {
        BSTFind<T> finindedNode = FindNodeByKey(key);

        if (!finindedNode.NodeHasKey) {
            return false;
        }

        BSTNode<T> nodeForDelete = finindedNode.Node;
        BSTNode<T> parentNode = nodeForDelete.Parent;

        if (nodeForDelete.LeftChild == null && nodeForDelete.RightChild == null) {

            if (parentNode == null) {
                Root = null;
            }

            else if (parentNode.LeftChild == nodeForDelete) {
                parentNode.LeftChild = null;
            }

            else {
                parentNode.RightChild = null;
            }

            return true;
        }

        if (nodeForDelete.LeftChild != null && nodeForDelete.RightChild != null) {

            BSTNode<T> nodeForMove =
                    FinMinMax(nodeForDelete.RightChild, false);

            nodeForDelete.NodeKey = nodeForMove.NodeKey;
            nodeForDelete.NodeValue = nodeForMove.NodeValue;


            BSTNode<T> nodeForMoveParent = nodeForMove.Parent;
            BSTNode<T> nodeForMoveChild = nodeForMove.RightChild;

            if (nodeForMoveParent.LeftChild == nodeForMove) {
                nodeForMoveParent.LeftChild = nodeForMoveChild;
            } else {
                nodeForMoveParent.RightChild = nodeForMoveChild;
            }

            if (nodeForMoveChild != null) {
                nodeForMoveChild.Parent = nodeForMoveParent;
            }

            return true;
        }

        BSTNode<T> child;

        if (nodeForDelete.LeftChild != null) {
            child = nodeForDelete.LeftChild;
        } else {
            child = nodeForDelete.RightChild;
        }

        if (parentNode == null) {
            Root = child;
            child.Parent = null;
        }

        else if (parentNode.LeftChild == nodeForDelete) {
            parentNode.LeftChild = child;
            child.Parent = parentNode;
        }
        else {
            parentNode.RightChild = child;
            child.Parent = parentNode;
        }

        return true;
    }

    public int Count()
    {
        return CountNodes(Root);
    }

    private int CountNodes(BSTNode<T> node) {
        if (node == null) {
            return 0;
        }

        return 1 + CountNodes(node.LeftChild) + CountNodes(node.RightChild);
    }
}