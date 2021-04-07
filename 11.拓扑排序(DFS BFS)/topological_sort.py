class DFSSolution:
    # DFS拓扑排序
    def findOrder(self, numCourses, prerequisites):
        if numCourses < 0:
            return []
        dic = {}  # pre: cur
        for i in range(len(prerequisites)):
            cur, pre = prerequisites[i]
            if pre not in dic:
                dic[pre] = []
            dic[pre].append(cur)

        valid = True
        flag = [0] * numCourses
        stack = []

        def dfs(u):
            nonlocal valid
            flag[u] = 1
            if u in dic:
                for v in dic[u]:
                    if flag[v] == 0:
                        dfs(v)
                        if valid == False:
                            return
                    elif flag[v] == 1:
                        valid = False
                        return
            flag[u] = 2
            stack.append(u)

        for i in range(numCourses):
            if valid and flag[i] == 0:
                dfs(i)
        if not valid:
            return []
        return stack[::-1]


class BFSSolution:
    # BFS拓扑排序
    def findOrder(self, numCourses, prerequisites):
        if numCourses < 0:
            return []
        edges = {}
        indges = [0] * numCourses
        for i in range(len(prerequisites)):
            cur, pre = prerequisites[i]
            if pre not in edges:
                edges[pre] = []
            edges[pre].append(cur)
            indges[cur] += 1

        queue = [i for i in range(numCourses) if indges[i] == 0]
        res = []
        while queue:
            u = queue.pop(0)
            res.append(u)
            if u in edges:
                for v in edges[u]:
                    indges[v] -= 1
                    if indges[v] == 0:
                        queue.append(v)
        return res if len(res) == numCourses else []


if __name__ == "__main__":

    obj1 = DFSSolution()
    print(obj1.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
    obj2 = BFSSolution()
    print(obj2.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))

