# https://leetcode.com/problems/inorder-successor-in-bst/ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.temp_list = []
        
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        self.in_order(root)
        temp_len = len(self.temp_list)
        #i = 0
        
        for i in range(temp_len):
            if self.temp_list[i] == p:
                if i < temp_len-1:
                    return self.temp_list[i+1]
                return None
            
    def in_order(self, root:'TreeNode'):
        if root is None:
            return
        self.in_order(root.left)
        self.temp_list.append(root)
        self.in_order(root.right)
        return
