# https://leetcode.com/problems/minimum-distance-between-bst-nodes/submissions/
'''
Runtime: 40 ms, faster than 56.40% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14 MB, less than 7.69% of Python3 online submissions for Minimum Distance Between BST Nodes.
'''
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        minDist = float('inf')
        list1 =[]
        print(list1)
        self.getInOrder(root, list1)
        return self.findMin(list1)
        
    def findMin(self, list1:list) -> int:
        prev = -1
        minDiff = float('inf')
        lenList1 = len(list1)
        for i in range(lenList1):
            if prev > 0 :
                diff = list1[i] - prev
                if diff < minDiff :
                    minDiff = diff
            
            prev = list1[i]
            
        return minDiff
        
    def getInOrder(self, root:TreeNode, list1:list) -> list:
        if root.left != None:
            self.getInOrder(root.left, list1)
        list1.extend([root.val])
        if root.right != None:
            self.getInOrder(root.right, list1)
        return list
        
