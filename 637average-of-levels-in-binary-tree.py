#https://leetcode.com/problems/average-of-levels-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            sum_level, count = 0, 0
            temp = []
            while len(queue)>0:
                n = queue.pop(0)
                sum_level += n.val
                count +=1
                if n.left != None:
                    temp.append(n.left)
                if n.right != None:
                    temp.append(n.right)
            queue = temp[:]
            res.append(sum_level /count)
        return res
