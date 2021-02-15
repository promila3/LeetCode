# https://leetcode.com/problems/is-graph-bipartite/
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeColor = {}
        lenGraph = len(graph)
        for i in range(lenGraph):
            if i not in nodeColor:
                stack = [i]
                nodeColor[i] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in nodeColor:
                            stack.append(neighbor)
                            nodeColor[neighbor] = nodeColor[node] ^1
                        elif nodeColor[neighbor] == nodeColor[node]:
                            return False
        return True
