################################# 双端队列及其应用：回文词判定 ################################

class Deque:
    '''
    定义双端队列的数据结构及相应操作
    '''
    # 初始化为空列表
    def __init__(self):
        self.items = []
    
    # 判断是否为空
    def isEmpty(self):
        return self.items == []
    
    # 从队尾入队
    def addRear(self,item):
        self.items.insert(0,item)
    
    # 从队首入队
    def addFront(self,item):
        self.items.append(item)
    
    # 从队首出队
    def removeFront(self):
        return self.items.pop()
    
    # 从队尾出队
    def removeRear(self):
        return self.items.pop(0)
    
    # 计算双端队列的大小
    def size(self):
        return len(self.items)


def parChecker(aString):
    '''
    判断aString是否为回文词
    
    输入：
        aString - 字符串，判断目标
        
    输出：
        isEqual - True/False，判断是否为回文词
    '''
    checkDeque = Deque()
    checkList = []
    isEqual = True
    
    for token in aString:
        checkDeque.addRear(token)
        
    while checkDeque.size() > 1 and isEqual:
        first = checkDeque.removeFront()
        last = checkDeque.removeRear()
        if first != last:
            isEqual = False
    
    return isEqual

# 测试
print(parChecker('aradara'))






