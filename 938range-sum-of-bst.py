# Definition for a binary tree node.
# https://leetcode.com/problems/range-sum-of-bst/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        #if root.val in range(low, high+1):
        if root.val < high +1 and root.val > low -1:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        else :
            return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
