'''
Runtime: 308 ms, faster than 25.46% of Python3 online submissions for Array Partition I.
Memory Usage: 15.2 MB, less than 6.06% of Python3 online submissions for Array Partition I.
561	
Array Partition I    
70.6%	Easy	
https://leetcode.com/problems/array-partition-i/submissions/
'''

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        numLen= len(nums)
        result = 0
        for i in range(0,numLen,2):
            result += min(nums[i],nums[i+1])
        return result
