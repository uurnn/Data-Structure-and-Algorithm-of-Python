class Stack:
    '''
    利用列表实现栈
    '''
    # 初始化栈为空列表
    def __init__(self):
        self.items = []
    
    # 入栈
    def push(self,item):
        self.items.append(item)
    
    # 出栈
    def pop(self):
        return self.items.pop()
    
    # 判断是否为空
    def isEmpty(self):
        return self.items == []
    
    # 查看栈顶元素（不出栈）
    def peek(self):
        return self.items[len(self.items) - 1]
    
    # 计算栈内元素的数量
    def size(self):
        return len(self.items)



