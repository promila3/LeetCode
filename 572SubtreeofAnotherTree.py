'''
Runtime: 244 ms, faster than 75.06% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions for Subtree of Another Tree.
https://leetcode.com/problems/subtree-of-another-tree/submissions/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def isdentical(s:TreeNode, t:TreeNode) -> bool:   
    if s is None and t is None:
        return True
        
    if s is None or t is None:
        return False
        
    if (s.val == t.val)and (isdentical(s.left,t.left) and isdentical(s.right, t.right)):
        return True
    else :
        return False
        
class Solution:
    
    #def dentical(self, s:TreeNode, t:TreeNode) -> bool:      

        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return true
        
        if s is None:
            return False
        
        if isdentical(s,t):
            return True
        
        result1 =  self.isSubtree(s.left, t)  or self.isSubtree( s.right, t) 
        
        return result1
    
