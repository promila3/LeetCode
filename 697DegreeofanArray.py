'''
Runtime: 244 ms, faster than 76.14% of Python3 online submissions for Degree of an Array.
Memory Usage: 14.1 MB, less than 27.27% of Python3 online submissions for Degree of an Array.
https://leetcode.com/problems/degree-of-an-array/
'''
class Solution:
    def getIndex(self, a:int, nums: List[int]) -> int:
        lenN = len(nums)
        for i in range(lenN):
            if a == nums[i]:
                first = i
                break
        for i in range(lenN-1,-1,-1):
            if a == nums[i]:
                last = i
                break  
        return first, last
            
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, countA = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: 
                left[x] = i 
            right[x] = i
            countA[x] = countA.get(x,0) + 1
        result =len(nums)
        degree = max(countA.values())
        for x in countA:
            if countA[x] == degree:
                result = min(result, right[x]- left[x] + 1)
        return result
