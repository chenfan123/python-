# 自定义代码模拟二叉树
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                current = queue.pop(0)
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
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.item, end=' ')
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    def preorder(self, node):
        if node is None:
            return
        print(node.item, end=' ')
        self.preorder(node.left)
        self.preorder(node.right)
        