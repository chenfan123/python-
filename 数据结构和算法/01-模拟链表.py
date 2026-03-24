# 单向链表
# 属于数据结构-线性结构的一种，每个节点只能有1个前驱1个后继节点
# 作用：用于优化顺序表的弊端，链表扩容时有地就行，连不连续无所谓
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
