from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        self.nodes = {}
        self.target = target
        for node in graph:
            if node[0] not in self.nodes:
                self.nodes[node[0]] = {node[1]}
            else:
                self.nodes[node[0]].add(node[1])
        for i in range(n):
            if i not in self.nodes:
                self.nodes[i] = set()
        # print(self.nodes)
        return self.dfs(start)

    def dfs(self, curr_node, searched_nodes=None):
        if searched_nodes is None:
            searched_nodes = set()
        # print(str(curr_node) + '->' + str(searched_nodes))
        if curr_node == self.target:
            # print(searched_nodes)
            return True
        if curr_node in searched_nodes:
            # print(searched_nodes)
            # print(curr_node)
            # print('loop')
            return False
        searched_nodes.add(curr_node)
        for nxt_node in self.nodes[curr_node]:
            # print(str(curr_node) + '->' + str(nxt_node))
            if self.dfs(nxt_node, searched_nodes):
                return True
        searched_nodes.remove(curr_node)
        # print('done')
        return False
