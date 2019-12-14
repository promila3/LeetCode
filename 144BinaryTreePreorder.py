'''
Runtime: 24 ms, faster than 94.66% of Python3 online submissions for Binary Tree Preorder Traversal.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.preOrder(root, result)
        return result
    
    def preOrder(self,root: TreeNode, result:List[int]) -> List[int]:
        if root == None:
            return []
        
        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
