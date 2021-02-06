#https://leetcode.com/problems/binary-tree-right-side-view/
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightside = []
        if root is None :
            return []
        nextLevel = [root]
        
        while len(nextLevel) > 0:
            currentLevel = nextLevel
            nextLevel = []
            while len(currentLevel) > 0:
                current = currentLevel.pop(0)
                if current.left:
                    nextLevel.append(current.left)
                if current.right:
                    nextLevel.append(current.right)
            rightside.append(current.val)
        return rightside
