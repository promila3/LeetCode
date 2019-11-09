'''
Runtime: 28 ms, faster than 99.83% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Minimum Cost Tree From Leaf Values.
'''

# https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/submissions/
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        current = 0
        while len(arr) > 0:
            arr, current = self.calc(arr, current)
        return current
    
    def calc(self, next: List[int], current) -> int:
        if len(next) <= 0:
            return [], current
        
        if len(next) == 2:
            current += next[0] * next[1]
            
            return [], current
        
        val = 0
        lenNext = len(next)
        selectVal = next[0] * next[1]
        selectIdx = 0
        for i in range(lenNext -1):
            curVal = next[i] * next[i+1]
            if selectVal > curVal:
                selectVal = curVal
                selectIdx = i
        current += selectVal
        newList = []
        i = 0
        while i < (lenNext):
            if i == selectIdx:
                newList.append(max(next[i],next[i+1]))
                i += 1
            else :
                newList.append(next[i])
            i +=1
                
        return newList, current
