"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        height = 0
        return self.dfs(root, height)
    def dfs(self, root:'Node', height:int)->int:
        if root is None:
            return height
        result = height +1
        for node in root.children:
            temp_height = self.dfs(node, height+1)
            result = max(temp_height, result)
        return result
