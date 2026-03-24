# 单向链表
# 属于数据结构-线性结构的一种，每个节点只能有1个前驱1个后继节点
# 作用：用于优化顺序表的弊端，链表扩容时有地就行，连不连续无所谓
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    def __init__(self,node=None):
        self.head = node # 链表的头节点


    def is_empty(self): # 判断链表是否为空
        return self.head is None

    def length(self): # 计算链表的长度
        current = self.head # 当前节点
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def travel(self):  # 遍历列表
        current = self.head
        while current is not None:
            print(current.item, end=' ')
            current = current.next
    
    def add(self, item):  # 在链表头部添加元素
        node = Node(item)
        node.next = self.head
        self.head = node
        
    def append(self, item):  # 在链表尾部添加元素
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        
    def insert(self, pos, item):  # 在指定位置插入元素
        node = Node(item)
        if pos == 0:
            node.next = self.head
            self.head = node
        elif pos>self.length():
            self.append(item) # 如果插入位置大于链表长度，则插入到链表尾部
        else:
            # 如果插入位置小于链表长度，则插入到指定位置
            pre = self.head
            count = 0
            while count < pos-1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
            
    def remove(self, item):  # 删除指定元素
        current = self.head
        pre = None
        while current is not None:
            # 找到删除节点
            if current.item == item:
                if current == self.head:
                    self.head = current.next
                else:
                    pre.next = current.next
                return
            else:
                pre = current
                current = current.next

    def search(self, item):  # 查找指定元素
        current = self.head
        while current is not None:
            if current.item == item:
                return True
            current = current.next
        return False
        
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.next = node2
    node2.next = node3
    print(f'元素域: {node1.item}, 链接域: {node1.next}')
    print(f'元素域: {node2.item}, 链接域: {node2.next}')
    ll = SingleLinkList(node1)
    print(ll.length())