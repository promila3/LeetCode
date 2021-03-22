# 98. Validate Binary Search Tree
#https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isValidBinary(node:TreeNode,left:int, right:int)-> bool:

            if node == None:
                return True
            if node.val <= left or node.val >= right:
                return False
            
            return (isValidBinary(node.right, node.val, right) and
                   isValidBinary(node.left, left, node.val))
            
        return isValidBinary(root, -math.inf, math.inf)
