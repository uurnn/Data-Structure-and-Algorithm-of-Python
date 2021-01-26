class Node:
    '''节点'''
    # 初始化节点，数据项为设定值，指针指向None
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    
    # 获得节点的数据项的值
    def getData(self):
        return self.data
    
    # 获得节点的指针指向
    def getNext(self):
        return self.next
    
    # 修改节点的数据项的值
    def setData(self,newdata):
        self.data = newdata
    
    # 修改节点的指针指向
    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:
    '''链表'''
    # 头指针初始化为None
    def __init__(self):
        self.head = None
    
    # 判断链表是否为空
    def isEmpty(self):
        return self.head == None
    
    # 链表中添加元素
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    # 计算链表的长度
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    # 寻找链表中的数据项
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found
    
    # 移除链表中的指定项
    def remove(self,item):
        current = self.head
        previous = None
            
        found = False
        
        while current != None and not found :
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


