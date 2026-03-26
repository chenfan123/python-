# 自定义代码模拟二叉树
class Node:
    """
    节点类
    """

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree:
    """
    二叉树
    """

    def __init__(self, node=None):
        self.root = node

    def add(self, item):
        """
        添加节点
        1. 初始化队列，将根结点入队，准备加入到二叉树的新节点
        2. 重复执行L获得并弹出队头元素；
            2.1 若当前节点的左右子节点不为空，则将其左右子节点入队列
            2.2 若当前节点的左右子节点为空，则将新节点挂到为空的左子节点或者右子节点
        """
        # 创建新节点
        node = Node(item)
        # 如果根节点为空，则将新节点作为根节点
        if self.root is None:
            self.root = node
            return
        # 如果根节点不为空，则将新节点加入到二叉树中，需要使用队列来实现
        else:
            # 初始化队列，将根结点入队，准备加入到二叉树的新节点
            queue = [self.root]
            # 通过死循环找到空缺的节点位置
            while queue:
                # 获得并弹出队头元素
                current = queue.pop(0)
                # 若当前节点的左右子节点不为空，则将其左右子节点入队列
                if current.left is None:
                    current.left = node
                    break
                else:
                    queue.append(current.left)
                if current.right is None:
                    current.right = node
                    break
                else:
                    queue.append(current.right)

    def breadth_travel(self):
        """
        广度遍历(逐层遍历)
        """
        if self.root is None:
            return
        # 队列
        queue = [self.root]
        # 通过死循环遍历队列中的元素
        while len(queue) > 0:
            # 获得并弹出队头元素
            current = queue.pop(0)
            print(current.item, end=' ')
            # 若当前节点的左子节点不为空，则将其左右子节点入队列
            if current.left is not None:
                queue.append(current.left)
            # 若当前节点的右子节点不为空，则将其右子节点入队列
            if current.right is not None:
                queue.append(current.right)

    def pre_order(self, node):
        """
        深度优先之先序遍历（根左右）
        """
        if node is None:
            return
        # 先打印根节点
        print(node.item, end=' ')
        # 再打印左子节点
        self.pre_order(node.left)
        # 最后打印右子节点
        self.pre_order(node.right)

    def in_order(self, node):
        "深度优先之中序遍历（左根右）"
        if node is None:
            return
        # 先打印左子节点
        self.in_order(node.left)
        # 再打印根节点
        print(node.item, end=' ')
        # 最后打印右子节点
        self.in_order(node.right)

    def post_order(self, node):
        "深度优先之后续遍历（左右根）"
        if node is None:
            return
        # 先打印左子节点
        self.post_order(node.left)
        # 再打印右子节点
        self.post_order(node.right)
        # 最后打印根节点
        print(node.item, end=' ')

    def dm01_t(self):
        node1 = Node(1)
        print(f'根节点: {node1.item}')
        print(f'左子节点: {node1.left.item}')
        print(f'右子节点: {node1.right.item}')
        bt = BinaryTree(node1)
        print(bt.root)
        print(bt.root.item)


if __name__ == '__main__':
    root = Node(0)
    print(f'根节点: {root.item}')
    print(f'左子节点: {root.left}')
    print(f'右子节点: {root.right}')
    tree = BinaryTree(root)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
