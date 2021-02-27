class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        n = 0
        for edge in edges:
            n = max(n, edge[0], edge[1])
        union_find = Solution.UnionFind(n)
        return []

    class UnionFind:
        def __init__(self, n):
            """
            :param n: int
            """
            self.pre = [i for i in range(n)]
            self.weight = [1 for i in range(n)]

        def union(self, a, b):
            """
            :param a: int
            :param b: int
            :return: None
            """
            root1 = self.find(a)
            root2 = self.find(b)
            if self.weight[root1] < self.weight[root2]:
                self.pre[root1] = root2
                self.weight[root2] += self.weight[root1]
            else:
                self.pre[root2] = root1
                self.weight[root1] += self.weight[root2]

        def find(self, a):
            """
            :param a: int
            :return: int
            """
            while self.pre[a] != a:
                a = self.pre[a]
            return a

        def is_connected(self, a, b):
            """
            :param a: int
            :param b: int
            :return: bool
            """
            return self.find(a) == self.find(b)
