'''
Runtime: 196 ms, faster than 84.67% of Python3 online submissions for Maximum Binary Tree.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Maximum Binary Tree.
'''
# https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        lenNums = len(nums)
        if lenNums == 0:
            return None
        maxNum = max(nums)
        maxIndex = nums.index(maxNum)
        # find the index of this number
        root = TreeNode(maxNum)
        left = self.constructMaximumBinaryTree(nums[:maxIndex])
        if maxIndex != lenNums -1 :
            right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        else :
            right = None
        root.left = left
        root.right = right
        return root
        
        
