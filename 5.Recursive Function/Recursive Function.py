'''递归: 记住是将问题分解成规模更小的相同问题'''


def sumList(numList):
    '''
    递归算法求解列表中的数列的和
    
    输入：
        numList - 目标数列
        
    最终返回：
        数列的和
    '''
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + sumList(numList[1:])


def toStr(n,base):
    '''
    递归算法实现任意进制转换，数n转换为base进制
    
    输入：
        n - 数
        base - 目标进制
    
    输出：
        转换结果，字符串
    '''
    table = "0123456789ABCDEF"
    if n < base:
        return table[n]
    else:
        return toStr(n//base,base) + table[n % base]


# 修改递归栈的深度
import sys
sys.getrecursionlimit()      # 获取栈的当前最大深度
sys.setrecursionlimit(1000)  # 修改栈的最大深度
sys.getrecursionlimit()      # 获取栈的当前最大深度


################################### 海龟作图系统绘制分形树 ##################################
def tree(branch_len):
    '''
    递归算法画分形树
    
    输入：
        branch_len - 树干长度
    
    返回：
        无，结果为画出分形树的图像
    '''
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        tree(branch_len - 15)
        t.left(40)
        tree(branch_len - 15)
        t.right(20)
        t.backward(branch_len)


'''
此处注释掉了，功能是分形树的绘制
import turtle
t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pensize(2)
t.pencolor('green')
tree(75)
t.hideturtle()
turtle.down()
'''


################################ 汉诺塔问题：僧侣搬盘子预测世界末日 ##############################
def moveTower(height, fromPole, withPole, toPole):
    '''
    将height个盘子从fromPole经withPole移动到toPole
    
    输入：
        height - 移动的盘子的深度
        fromPole - 开始柱,'#1'
        withPole - 中间柱,'#2'
        toPole - 目标柱,'#3'
        
    返回：
        无，结果显示盘子的移动过程
    '''
    if height >= 1:
        moveTower(height-1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, fromPole, toPole)


def moveDisk(disk, fromPole, toPole):
    '''
    将一个盘子从开始柱移动到目标柱
    
    输入：
        disk - 移动的盘子
        fromPole - 开始柱
        withPole - 中间柱
        
    返回：
        无，显示一个盘子的移动过程
    '''
    print('Moving disk[{}] from {} to {}'.format(disk, fromPole, toPole))


# 测试
moveTower(10, '#1', '#2', '#3')


############################# 递归算法和动态规划算法 求解硬币找零问题 ################################
def recDc(numList, change, knowResult):
    '''
    递归算法实现硬币找零
    
    输入：
        numList - 列表，包含硬币面值
        change - 实数，找零总钱
        knowResult - 列表，记录找零的部分最优解，即一定面值下的最优找零个数
        
    返回：
        minCoins - 最少找零硬币个数
    '''
    minCoins = change
    if change in numList:
        knowResult[change] = 1
        return 1
    elif knowResult[change] > 0 :
        return knowResult[change]
    else:
        for i in [c for c in numList if c <= change]:
            numCoins = 1 + recDc(numList, change - i, knowResult)
            if minCoins > numCoins:
                minCoins = numCoins
                knowResult[change] = minCoins
    return minCoins


def dpMakeChange(valueList, change, minCoins, coinUsed):
    '''
    动态规划算法实现硬币找零
    
    输入：
        valueList - 列表，硬币所有面值
        change - 实数，找零钱数
        minCoins - 列表，在对应面值时最小找零硬币个数
        coinUsed - 列表，记录使用哪个硬币找零
        
    输出：
        minCoins[change] - 实数，最小找零个数
    '''    
    for cent in range(1, change + 1):
        coinCount = cent
        newCoin = 1
        for j in [c for c in valueList if c <= cent]:
            if minCoins[cent - j] + 1 < coinCount:
                coinCount = minCoins[cent - j] + 1 
                newCoin = j
        minCoins[cent] = coinCount

    return minCoins[change]


#########递归算法和动态规划算法解决 博物馆大盗问题：在一定的负重范围内偷取最大价值的文物 #############
'''
动态规划解决博物馆大盗问题
'''
# 列表存储文物的价值和重量
tr = [None, {'w':2, 'v':3}, {'w':3, 'v':4}, {'w':4, 'v':8}, {'w':5, 'v':8}, {'w':9, 'v':10}]
    
# 盗贼最大负重
max_w = 20
    
# 初始化价值字典
m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}
    
# 从小问题的解决开始，向大问题演变
for i in range(1,len(tr)):
    for w in range(1, max_w + 1):
        # 如果第i个文物的重量大于背包负重，则不装第i个，总价值等于不装第i个时的价值
        if tr[i]['w'] > w:
            m[(i,w)] = m[(i-1,w)]
        # 否则，能装第i个文物，装载最大价值等于 装入i文物前 和 装入i文物后  的价值的最大值
        else:
            m[(i,w)] = max(m[(i-1,w)], m[(i-1,w-tr[i]['w'])] + tr[i]['v'])


'''
递归法解决博物馆大盗问题
'''
thing = {(2,3),(3,4),(4,8),(5,8),(9,10)}
max_w = 20
m = {}

def thief(thing, w):
    '''
    递归算法
    
    输入：
        thing - 宝物集合，元素为元组，包含每个宝物的重量和价值
        w - 最大负重
        
    输出：
        vmax - 偷盗的最大价值
    '''
    if thing == set() or w == 0:
        m[(tuple(thing), w)] = 0
        return 0
    elif (tuple(thing),w) in m:
        return m[(tuple(thing), w)]
    else:
        vmax = 0
        for t in thing:
            if t[0]<= w:
                v = thief(thing - {t}, w - t[0]) + t[1]
                vmax = max(v, vmax)
        m[(tuple(thing), w)] = vmax
        return vmax


