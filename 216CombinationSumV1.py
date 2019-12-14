# https://leetcode.com/problems/combination-sum-iii/
'''
Runtime: 36 ms, faster than 62.72% of Python3 online submissions for Combination Sum III.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Combination Sum III.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        mapSet = set()
        
        self.dfs(k, n, mapSet, result,1)
        return result
    
    def dfs(self, k:int,n:int, mapSet:set(), result:List[List[int]], currentNum):
        if k == 0 and n == 0:
            result.append(list(mapSet))
            
        if k <= 0 or n <= 0 :
            return
        
        for i in range(currentNum, 10):
            mapSet.add(i)
            self.dfs(k-1,n-i,mapSet, result, i+1)
            mapSet.remove(i)
        
