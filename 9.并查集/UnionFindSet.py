class UnionFindSet(object):
    """并查集，森林表示图的动态连通性，用数组/字典等数据结构实现"""

    def __init__(self, nodes):
        self.count = 0
        self.father = {}
        self.size = {}
        for node in nodes:
            self.father[node] = node
            self.size[node] = 1
            self.count += 1

    def find(self, node):
        """找到node的根节点，同时路径压缩"""
        while self.father[node] != node:
            self.father[node] = self.father[self.father[node]]
            # 路径压缩，使union()方法的时间复杂度降到O(1)
            node = self.father[node]
        return node

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return
        if self.size[rootP] > self.size[rootQ]:
            self.father[rootQ] = rootP
            self.size[rootQ] += self.size[rootP]
        else:
            self.father[rootP] = rootQ
            self.size[rootP] += self.size[rootQ]
        self.count -= 1


if __name__ == '__main__':

    nodes = ['knn', 'lr', 'xgb', 'lgb', 'tree', 'svm', 'nb']

    union_find = UnionFindSet(nodes)
    union_find.union('lr', 'svm')
    union_find.union('lr', 'nb')
    union_find.union('tree', 'xgb')
    union_find.union('xgb', 'lgb')

    print(union_find.connected('svm', 'nb'))    # True
    print(union_find.connected('tree', 'lgb'))  # True
    print(union_find.connected('knn', 'xgb'))   # False



