class Queue:
    '''
    利用列表定义队列及相应操作
    '''
    # 初始化队列为空列表
    def __init__(self):
        self.items = []
    
    # 入队
    def enqueue(self,item):
        self.items.insert(0,item)
      
    # 出队
    def dequeue(self):
        return self.items.pop()
    
    # 判断是否为空
    def isEmpty(self):
        return self.items == []
    
    # 计算队列的长度
    def size(self):
        return len(self.items)

############################## 队列实例：模拟打印机系统的工作模式 ############################
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
        
    def tick(self):                # 打印一秒
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):                # 判断是否忙
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self,newtask):   # 开始新任务
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
        
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    '''
    以概率创建新任务
    
    输入：
        无
        
    输出：
        True/False - 是否有新任务被创建
    '''
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):
    '''
    模拟打印机工作,记录作业平均等待时间
    
    输入：
        numSeconds - 打印机模拟总时间
        pagesPerMinute - 打印机打印速度，页/分、
        
    输出：
        aveWait - 平均等待时间
    '''
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
            
        if (not labprinter.busy() and  not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(task.waitTime(currentSecond))
            
            labprinter.startNext(nexttask)
        
    print("平均等待时间： {}， {}个任务正在等待".format(np.mean(waitingtimes), printQueue.size()))


# 测试
for i in range(10):
    simulation(3600,5)




