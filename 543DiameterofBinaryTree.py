'''
Runtime: 744 ms, faster than 5.10% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
'''
# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def height(self, root:TreeNode)-> int:
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        return (1 + max(lheight,rheight))
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiameter = self.diameterOfBinaryTree(root.right)
        
        return max(lheight+rheight, lDiameter, rDiameter)
        
        
