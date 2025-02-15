# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# to add complexity
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levels = []
        next_level = deque([root])
        while root and next_level:
            curr_level = next_level
            next_level  = deque()
            levels.append([])
            for node in curr_level:
                levels[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
        return levels[::-1]
