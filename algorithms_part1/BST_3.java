public class BST_3 {
    public static void main(String[] args) {
        // Тесты добавления узлов
        BST<Integer> tree = new BST<>(null);
        tree.AddKeyValue(10, 100);
        tree.AddKeyValue(5, 50);
        assert tree.Root.LeftChild.NodeKey == 5;
        assert tree.Root.LeftChild.NodeValue == 50;


        // Проверка добавления вправо
        tree = new BST<>(null);
        tree.AddKeyValue(10, 100);
        tree.AddKeyValue(20, 200);
        assert tree.Root.RightChild.NodeKey == 20;
        assert tree.Root.RightChild.NodeValue == 200;

        // Проверка добавления на более низкий уровень
        tree = new BST<>(null);
        tree.AddKeyValue(10, 100);
        tree.AddKeyValue(5, 50);
        tree.AddKeyValue(7, 70);
        tree.AddKeyValue(14, 33);
        assert tree.Root.LeftChild.RightChild.NodeKey == 7;
        assert tree.Root.RightChild.NodeKey == 14;

        // Проверка добавления ключа который уже есть
        tree = new BST<>(null);
        tree.AddKeyValue(10, 100);
        tree.AddKeyValue(5, 50);
        tree.AddKeyValue(7, 70);
        tree.AddKeyValue(14, 33);
        tree.AddKeyValue(14, 55);
        assert !tree.AddKeyValue(14, 55);

        // Тесты поиска по дереву
        tree = new BST<>(null);

        tree.AddKeyValue(10, 100);
        tree.AddKeyValue(5, 50);
        tree.AddKeyValue(20, 200);
        tree.AddKeyValue(7, 70);


        // поиск корня
        BSTFind<Integer> result = tree.FindNodeByKey(10);
        assert result.NodeHasKey;
        assert result.Node.NodeKey == 10;
        assert result.Node.NodeValue == 100;


        // поиск узла в глубине дерева
        result = tree.FindNodeByKey(7);
        assert result.NodeHasKey;
        assert result.Node.NodeKey == 7;
        assert result.Node.NodeValue == 70;


        // ключ отсутсвует, но новый узел должен быть слева
        result = tree.FindNodeByKey(3);
        assert !result.NodeHasKey;
        assert result.Node.NodeKey == 5;
        assert result.ToLeft;


        // ключ отсутсвует, но новый узел должен быть справа
        result = tree.FindNodeByKey(8);
        assert !result.NodeHasKey;
        assert result.Node.NodeKey == 7;
        assert !result.ToLeft;


        // поиск в пустом дереве
        tree = new BST<>(null);
        result = tree.FindNodeByKey(10);
        assert !result.NodeHasKey;
        assert result.Node == null;

        // Тесты поиска максимального и минимального ключа
        tree = new BST<>(null);

        tree.AddKeyValue(4, 12);
        tree.AddKeyValue(2, 33);
        tree.AddKeyValue(5, 1);
        tree.AddKeyValue(1, 5);
        tree.AddKeyValue(9, 16);

        // поиск начиная с корня дерева Ищем максимум
        BSTNode<Integer> maxNode = tree.FinMinMax(tree.Root, true);
        assert maxNode.NodeKey == 9;
        assert maxNode.NodeValue == 16;

        // поиск начиная с корня дерева Ищем минимум
        BSTNode<Integer> minNode = tree.FinMinMax(tree.Root, false);
        assert minNode.NodeKey == 1;
        assert minNode.NodeValue == 5;

        // ищем минимум в под дереве слева
        BSTNode<Integer> leftMinNode = tree.FinMinMax(tree.Root.LeftChild, false);

        assert leftMinNode != null;
        assert leftMinNode.NodeKey == 1;

        // ищем максимум в левом поддереве
        BSTNode<Integer> leftMaxNode = tree.FinMinMax(tree.Root.LeftChild, true);

        assert leftMaxNode != null;
        assert leftMaxNode.NodeKey == 2;

        // ищем минимум в под дереве справа
        BSTNode<Integer> rightMinNode = tree.FinMinMax(tree.Root.RightChild, false);

        assert rightMinNode != null;
        assert rightMinNode.NodeKey == 5;

        // ищем максимум в правом поддереве
        BSTNode<Integer> rightMaxNode = tree.FinMinMax(tree.Root.RightChild, true);

        assert rightMaxNode != null;
        assert rightMaxNode.NodeKey == 9;


        BST<Integer> treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);
        treeForDelete.AddKeyValue(20, 200);

        assert !treeForDelete.DeleteNodeByKey(99);
        assert treeForDelete.Count() == 3;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);
        treeForDelete.AddKeyValue(20, 200);
        treeForDelete.AddKeyValue(7, 70);

        assert treeForDelete.DeleteNodeByKey(7);

        assert treeForDelete.Count() == 3;
        assert treeForDelete.Root.NodeKey == 10;
        assert treeForDelete.Root.LeftChild.NodeKey == 5;
        assert treeForDelete.Root.RightChild.NodeKey == 20;

        assert treeForDelete.Root.LeftChild.RightChild == null;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);

        assert treeForDelete.DeleteNodeByKey(10);

        assert treeForDelete.Root == null;
        assert treeForDelete.Count() == 0;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);
        treeForDelete.AddKeyValue(3, 30);

        assert treeForDelete.DeleteNodeByKey(5);

        assert treeForDelete.Count() == 2;
        assert treeForDelete.Root.LeftChild.NodeKey == 3;
        assert treeForDelete.Root.LeftChild.Parent == treeForDelete.Root;
        assert treeForDelete.Root.RightChild == null;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);
        treeForDelete.AddKeyValue(7, 70);

        assert treeForDelete.DeleteNodeByKey(5);

        assert treeForDelete.Count() == 2;
        assert treeForDelete.Root.LeftChild.NodeKey == 7;
        assert treeForDelete.Root.LeftChild.Parent == treeForDelete.Root;
        assert treeForDelete.Root.RightChild == null;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);

        assert treeForDelete.DeleteNodeByKey(10);

        assert treeForDelete.Root.NodeKey == 5;
        assert treeForDelete.Root.Parent == null;
        assert treeForDelete.Count() == 1;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(20, 200);
        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(30, 300);
        treeForDelete.AddKeyValue(25, 250);
        treeForDelete.AddKeyValue(40, 400);

        assert treeForDelete.DeleteNodeByKey(30);

        assert treeForDelete.Count() == 4;

        assert treeForDelete.Root.RightChild.NodeKey == 40;
        assert treeForDelete.Root.RightChild.NodeValue == 400;

        assert treeForDelete.Root.RightChild.Parent == treeForDelete.Root;
        assert treeForDelete.Root.RightChild.LeftChild.NodeKey == 25;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(20, 200);
        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(30, 300);
        treeForDelete.AddKeyValue(25, 250);
        treeForDelete.AddKeyValue(35, 350);
        treeForDelete.AddKeyValue(23, 230);

        assert treeForDelete.DeleteNodeByKey(20);

        assert treeForDelete.Count() == 5;

        assert treeForDelete.Root.NodeKey == 23;
        assert treeForDelete.Root.NodeValue == 230;

        assert treeForDelete.Root.Parent == null;
        assert treeForDelete.Root.LeftChild.NodeKey == 10;
        assert treeForDelete.Root.RightChild.NodeKey == 30;

        assert treeForDelete.Root.RightChild.LeftChild.NodeKey == 25;

        treeForDelete = new BST<>(null);

        treeForDelete.AddKeyValue(10, 100);
        treeForDelete.AddKeyValue(5, 50);
        treeForDelete.AddKeyValue(20, 200);
        treeForDelete.AddKeyValue(15, 150);
        treeForDelete.AddKeyValue(30, 300);

        assert treeForDelete.DeleteNodeByKey(10);

        assert treeForDelete.Count() == 4;

        assert treeForDelete.Root.NodeKey == 15;
        assert treeForDelete.Root.NodeValue == 150;

        assert treeForDelete.Root.Parent == null;
        assert treeForDelete.Root.LeftChild.NodeKey == 5;
        assert treeForDelete.Root.RightChild.NodeKey == 20;
    }
}
