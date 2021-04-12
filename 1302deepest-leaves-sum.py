# https://leetcode.com/problems/deepest-leaves-sum/ 
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def get_height(root:TreeNode)->int:
            if root == None:
                return 0
            return max(get_height(root.left)+1, get_height(root.right)+1)
        def get_sum(root:TreeNode, level:int)->int:
            if root == None:
                return
            if level == height:
                self.result += root.val
            get_sum(root.left, level+1)
            get_sum(root.right, level+1)
            return
            
        height = get_height(root)
        
        get_sum(root,1)  
        return self.result
