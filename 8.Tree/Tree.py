import operator

class BinaryTree:
    '''
    利用链表构建树结构
    '''
    def __init__(self, data):
        self.val = data
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, newNode):
        '''向根插入左子节点'''
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        '''向根插入右子节点'''
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getLeftChild(self):
        '''获得左子树'''
        return self.leftChild
    
    def getRightChild(self):
        '''获得右子树'''
        return self.rightChild
    
    def getRootVal(self):
        '''获得根节点的值'''
        return self.val
    
    def setRootVal(self, obj):
        '''修改根节点的值'''
        self.val = obj
        
    def beforeOrder(self):
        '''先序遍历'''
        print(self.val)
        if self.leftChild:
            self.beforeOrder(self.leftChild)
        if self.rightChild:
            self.beforeOrder(self.rightChild)
    
    def betweenOrder(self):
        '''中序遍历'''
        if self.leftChild:
            self.betweenOrder(self.leftChild)
        print(self.val)
        if self.rightChild:
            self.betweenOrder(self.rightChild)

    def afterOrder(self):
        '''后序遍历'''
        if self.leftChild:
            self.afterOrder(self.leftChild)
        if self.rightChild:
            self.afterOrder(self.rightChild)
        print(self.val)


def preorder(Tree):
    '''
    前序遍历，根左右
    '''
    if Tree != None:
        print(Tree.getRootVal())
        preorder(Tree.getLeftChild())
        preorder(Tree.getRightChild())


def inorder(Tree):
    '''
    中序遍历，左根右
    '''
    if Tree != None:
        inorder(Tree.getLeftChild())
        print(Tree.getRootVal())
        inorder(Tree.getRightChild())


def postorder(Tree):
    '''
    后序遍历，左右根
    '''
    if Tree != None:
        postorder(Tree.getLeftChild())
        postorder(Tree.getRightChild())
        print(Tree.getRootVal())



