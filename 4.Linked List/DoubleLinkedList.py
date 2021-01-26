class Node(object):
    def __init__(self, data=None):
        self.val = data
        self.next = None
        self.pre = None


class DoubleLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def add_last(self, data):
        node = Node(data)
        self.tail.pre.next = node
        node.pre = self.tail.pre
        self.tail.pre = node
        node.next = self.tail
        self.size += 1

    def get(self, index):
        """获取链表第index的节点，大于0正向获取，小于0反向获取"""
        index = index if index > 0 else self.size + index
        if index > self.size or index < 0:
            return None
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node

    def set_data(self, index, data):
        node = self.get(index)
        if node:
            node.val = data
        return node

    def insert(self, index, data):
        if index > self.size:
            return False
        next_node = self.get(index)
        if next_node:
            node = Node(data)
            next_node.pre.next = node
            node.pre = next_node.pre
            node.next = next_node
            next_node.pre = node
            self.size += 1

    def remove(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            self.size -= 1

    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0


if __name__ == '__main__':

    test_link = DoubleLinkedList()

    test_link.add_last(5)
    test_link.add_last(3)
    print(test_link.size)

    test_link.remove(1)
    print(test_link.size)

    test_link.clear()
    print(test_link.size)
