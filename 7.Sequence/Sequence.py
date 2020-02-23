########################################### 冒泡排序 ###########################################
'''
思想：若有n个数待排序，则比较n-1趟，在每趟中相邻两元素进行比较，逆序则交换次序。
      每趟比较会“浮出”一个最大值或最小值。
时间复杂度：O(n^2)
'''

def bubbleSort(alist):
    '''
    冒泡排序
    
    输入：
        alist - 待排序的无序表
        
    输出：
        排序后的有序表
    '''
    # n个数比n-1趟，每趟冒出一个最大值，即每趟将一个最大值移至列表最后
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist [i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

# 测试
print(bubbleSort([15,2,4,1,6,8,5,95,0]))

def shortBubbleSort(alist):
    '''
    冒泡排序的改进 -- 通过判断在每一趟冒泡中是否发生数据交换，来判断排序是否提前完成
    
    输入：
        alist - 待排序的无序表
        
    输出：
        排序后的有序表
    '''
    exchange = True
    passnum = len(alist) - 1
    
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]
        passnum -= 1
    return alist

# 测试
print(shortBubbleSort([15,2,4,1,6,8,5,95,0]))

########################################### 选择排序 #########################################
'''
思想：冒泡排序的改进，在每一趟比较中，选择最大或最小的值与未排序的最前面的值进行交换，每一趟比较只进行一次交换。
时间复杂度：O(n^2)
'''

def selectionSort(alist):
    '''
    选择排序 -- 冒泡排序的改进，每一趟只交换一次
    
    输入：
        alist - 待排序的无序表
        
    输出：
        排序后的有序表
    '''
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[positionOfMax], alist[fillslot] = alist[fillslot], alist[positionOfMax]
    
    return alist

# 测试
print(selectionSort([15,2,4,1,6,8,5,95,0]))

######################################### 插入排序 #############################################
'''
思想：维持子列表始终有序。每次从无序的子列表中选出一个数，放在有序子列表内的正确位置处，保证有序子列表始终有序。
时间复杂度：O(n^2)
'''

def insertSort(alist):
    '''
    插入排序 -- 维持已排序的字列表，每次从无序列表中取出一个数，插入到顺序正确的位置
    
    输入：
        alist - 待排序的无序表
        
    输出：
        排序后的有序表
    '''
    for index in range(1,len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentValue
    return alist

# 测试
print(insertSort([15,2,4,1,6,8,5,95,0]))


######################################## 希尔排序 ###########################################
'''
思想：插入排序的改进。按间隔将列表分为子列表，子列表数与间隔相等，随后对每个子列表进行插入排序。
      间隔从n//2开始，每次缩小一半，直至间隔为1。此时子列表就是整个列表，它是近似有序的，进行插入排序时时间复杂度较低。
时间复杂度：O(n^1.5)
'''

def shellSort(alist):
    '''
    希尔排序 
        -- 希尔排序是基于插入排序，先将列表按间隔分为字列表，再对字列表进行插入排序。间隔从n/2、n/4、…，一直减小到1
    
    输入：
        alist - 待排序的列表
        
    输出：
        排序后的列表
    '''
    # 定义子列表间隔
    subListGap = len(alist) // 2
    
    # 对所有字列表进行插入排序
    while subListGap > 0:
        # 遍历字列表，字列表的数量 等于 字列表之间的间隔
        for startPosition in range(subListGap):
            # 调用函数：带间隔的插入排序
            gapInsertSort(alist, startPosition, subListGap)
        
        subListGap = subListGap // 2
    return alist       

def gapInsertSort(alist, start, gap):
    '''
    在整个列表alist上，对带间隔的子列表进行插入排序
    
    输入：
        alist - 待排序的原列表
        start - 字列表的起始位置
        gap - 字列表之间的间隔
    
    输出：
        字列表全部排完序后的列表
    '''
    # 对起始位置在start处的字列表进行插入排序
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        
        while position >= gap and currentValue < alist[position - gap]:
            alist[position] = alist[position - gap]
            position = position - gap
        
        alist[position] = currentValue
    
    return alist

# 测试
print(shellSort([15,2,4,1,6,8,5,95,0]))


##################################### 归并排序 #####################################
'''
思想：不断将列表分成左半部分和右半部分，直至每一部分只剩一个元素，此时每一部分已排好序。
      再进行归并操作，即拉链式的交错归并。
过程：1.分裂  2.归并
实现：递归算法。
'''

def mergeSort(alist):
    '''
    归并排序的传统方法
    
    输入：
        alist - 待排序的列表
        
    输出：
        alist - 排序后的列表
    '''
    # 停止条件    
    if len(alist) > 1:
        mid = len(alist) // 2
        leftHalf = alist[: mid]
        rightHalf = alist[mid :]
        # 递归调用本身
        mergeSort(leftHalf)
        mergeSort(rightHalf)
    
        # 设定索引i、j、k，分布控制左半部分、右半部分、合成部分的元素索引
        i = j = k = 0
    
        # 拉链式交错，把左半部分和右半部分从小到大归并到结果列表中
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                alist[k] = leftHalf[i]
                i += 1
            else:
                alist[k] = rightHalf[j]
                j += 1
            k += 1
    
        # 当归并后，右半部分为空，左半部分有剩余
        while i < len(leftHalf):
            alist[k] = leftHalf[i]
            i += 1
            k += 1
        
        # 当归并后，左半部分为空，右半部分有剩余
        while j < len(rightHalf):
            alist[k] = rightHalf[j]
            j += 1
            k += 1
    
    return alist

# 测试
print(mergeSort([15,2,4,1,6,8,5,95,0]))

def merge_Sort(alist):
    '''
    归并排序，更具有python风格的归并排序的代码
    
    输入：
        alist - 待排序的列表
        
    输出：
        merged - 排序后的列表
    '''
    # 停止条件
    if len(alist) <= 1:
        return alist
    
    midPosition = len(alist) // 2
    leftHalf = merge_Sort(alist[: midPosition])
    rightHalf = merge_Sort(alist[midPosition :])

    merged = []
    while leftHalf and rightHalf:
        if leftHalf[0] < rightHalf[0]:
            merged.append(leftHalf.pop(0))
        else:
            merged.append(rightHalf.pop(0))
    
    merged.extend(rightHalf if rightHalf else leftHalf)
    
    return merged

# 测试
print(merge_Sort([15,2,4,1,6,8,5,95,0]))


###################################### 快速排序 ######################################
'''
思想：利用合适的“中值”，将列表分裂为左右两部分，再对左右两部分分别递归调用快速排序算法（递归调用快排算法）
实现：1.分裂 2.递归调用
关键：“中值”的选取，可用三点采样法
'''

def quickSort(alist):
    '''
    快速排序
    
    输入：
        alist - 待排序的列表
        
    输出：
        无
        
    注释：
        此函数中调用 快速排序助手函数，因为快速排序的输入仅是单个列表，而快速排序的递归调用中需要传递快排的范围。
    '''
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelp(alist, first, last):
    '''
    快速排序助手，对alist在first和last之间的数进行快速排序
    
    输入：
        alist - 待排序的列表
        first - 快速排序范围的起始位置
        last - 快速排序范围的终止位置
        
    输出：
        无
    '''
    if first < last:
        splitPosition = partition(alist, first, last)
        
        quickSortHelper(alist, first, splitPosition - 1)
        quickSortHelper(alist, splitPosition + 1, last)
    return alist


def partition(alist, first, last):
    '''
    根据中值，将列表分裂成大小两部分
    
    输入：
        alist - 待分裂的列表
        first - 分裂范围的首位置
        last - 分裂范围的尾位置
        
    输出：
        splitPosition - 分裂点
    '''
    midValue = alist[first]
    
    # 此步是快排算法的关键。定义左右标记，用于后续值的交换。
    leftMark = first + 1
    rightMark = last
    
    # 设置done，记录是否完成本次分裂
    done = False
    
    while not done:
        
        # 此处是以列表中的第一个数为中值
        
        # 左标记右移
        while leftMark <= rightMark and alist[leftMark] <= midValue:
            leftMark += 1
            
        # 右标记左移
        while rightMark >= leftMark and alist[rightMark] >= midValue:
            rightMark -= 1
            
        if leftMark > rightMark:
            done = True
        else:
            alist[rightMark], alist[leftMark] = alist[leftMark], alist[rightMark]
            
    alist[first], alist[rightMark] = alist[rightMark], alist[first]
            
    splitPosition = rightMark
    
    return splitPosition


# 测试
alist = [15,2,4,1,6,8,5,95,0]
quickSort(alist)
alist





