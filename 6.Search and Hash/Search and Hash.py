#################################### 顺序查找：查找无序表和有序表 ####################################
'''
思想：通过下标，按顺序查找数据项
时间复杂度：O(n)
'''

def searchUnorder(alist, item):
    '''
    顺序查找无序表，时间复杂度为O（n）
    
    输入：
        alist - 列表，查找的目标列表
        item - 实数，查找的数据项
        
    返回：
        found - True/False，是否找到
    '''
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
            
    return found

# 测试
print(searchUnorder([1,2,3,4,5,6,7], 8))


def searchOrder(alist, item):
    '''
    顺序查找有序表，时间复杂度为O（n）
    
    输入：
        alist - 有序列表，从小到大，查找的目标列表
        item - 实数，查找的数据项
        
    返回：
        found - True/False，是否找到
    '''
    pos = 0
    found = False
    stop = False
    
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos += 1
    
    return found


# 测试
print(searchOrder([1,2,3,4,5,6,7], 1))


######################################### 二分查找：有序表 ##########################################
'''
思想：针对有序表。每次比较查找值和表的中间项，若不相等，则缩小查找范围，继续进行二分查找。
实现：可用常规算法流程编程，也可用递归算法。
时间复杂度：O(nlog n)
'''

def binarySearchUsual(alist, item):
    '''
    二分查找算法，查找有序表
    
    输入：
        alist - 有序列表，从小到大，查找的目标列表
        item - 实数，查找的数据项
        
    返回：
        found - True/False，是否找到
    '''
    first = 0
    last = len(alist) - 1
    found = False
    
    while first <= last and not found:
        midPoint = (first + last) // 2
        if alist[midPoint] == item:
            found = True
        else:
            if alist[midPoint] > item:
                last = midPoint - 1
            else:
                first = midPoint + 1
    
    return found

# 测试
print(binarySearchUsual([1,2,13,24,35,36,47], 13))


def binarySearchRec(alist, item):
    '''
    递归算法实现二分查找
    
    输入：
        alist - 有序列表，从小到大，查找的目标列表
        item - 实数，查找的数据项
        
    返回：
        found - True/False，是否找到
    '''
    if len(alist) == 0:
        return False
    else:
        midPoint = len(alist) // 2
        if alist[midPoint] == item:
            return True
        else:
            if item < alist[midPoint]:
                return binarySearchRec(alist[ : midPoint], item)
            else:
                return binarySearchRec(alist[midPoint+1 :], item)


# 测试
print(binarySearchRec([1,2,13,24,35,36,47], 13))


############################################ 散列 ###############################################
'''
散列：
    散列是一种数据集，可以通过其存储方式快速对数据项进行定位和查找。
    散列中，每个数据项存储的位置成为槽（slot），每个槽有唯一的名称。
    可以根据槽的名称--键（key）直接访问在存储空间的数据。

散列函数：
    实现从数据项到槽名称的转换，即将各个数据项映射到不同的槽中。
    因为散列表的长度一般固定，因此不同的数据利用相同的散列函数映射后，得到的散列值的长度相同。
    散列函数可以将不同的数据映射到相同长度的数据。说白了，是将数据压缩为固定长度的散列值，类似于数据的“指纹”。

散列存在的问题：
    冲突问题，即不同的数据项可能映射到同一个槽中。
    解决办法：1.开放定址技术。寻找其他空槽存放数据。缺点是影响其他数据项的插入。
              2.数据项链。将数据按顺序挂到同一槽中。

完美散列函数：
    不会导致冲突问题的散列函数。
    近似的完美散列函数包括：MD5（128位），SHA-0/SHA-1（20字节），SHA-256（256位），SHA-224（224位），SHA-512（512位），SHA-384（384位）
                            其中，括号内为映射后的数据长度，二进制位数。

散列函数用途：
      1.查找数据项。通过比较散列值，快速查找数据项，时间复杂度O（1），关键问题在于冲突问题的解决。
      2.校验数据的一致性。通过比较两个数据的散列值（指纹）是否相同，校验两份数据是否一致。
      3.密码加密。通过比较输入密码和正确密码的散列值，判断密码是否正确。
      4.……
'''

# 引入Python中的散列函数模块
import hashlib

# 例1，以16进制形式输出"hello world!"的md5散列值
print(hashlib.md5("hello world!".encode("utf-8")).hexdigest())  # 注意，.encode("utf-8")指定编码格式

# 例2，可用update（）对任意长的数据部分进行计算
m = hashlib.md5()
m.update("hello world!".encode("utf-8"))
print(m.hexdigest())


############################################### 映射 ##################################################
'''
映射的结构：键-值关联的无序集合，即Python中的字典。
实现：此处利用散列表实现映射的数据结构，可以快速查找目标数据项。
'''

class HashTable:
    '''利用散列表（哈希表）实现映射'''
    # 初始化，slots列表存放槽名称（key），data列表存放数据项，两个列表的相应位置一一对应。
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    # 求余法实现散列函数
    def hashFunction(self, key):
        return key % self.size
    
    # 散列冲突时，再散列，用其他空槽存储数据
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size
    
    # 存放数据项和槽名称。
    def put(self, key, data):
        hashValue = self.hashFunction(key)
        
        # 若key不存在，无冲突
        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            # 若key存在,则修改数据
            if self.slots == key:
                self.data[hashValue] = data
            else:
                # 散列冲突，再散列，直到找到空槽或key。
                nextSlot = self.rehash(hashValue)
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot)
                # 若是空槽
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data 
    
    # 获取指定槽（key）的数据
    def get(self, key):
        startSlot = self.hashFunction(key)
        
        data = None
        stop = False
        found = False
        position = startSlot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startSlot:
                    stop = True
        return data
                    
    # 特殊方法实现[]访问
    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        self.put(key,data)




