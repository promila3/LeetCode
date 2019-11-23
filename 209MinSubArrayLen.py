'''
Runtime: 72 ms, faster than 97.91% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 15.3 MB, less than 7.69% of Python3 online submissions for Minimum Size Subarray Sum.
https://leetcode.com/problems/minimum-size-subarray-sum/
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        currSum = 0
        minLen = n  +1
        
        

        start = 0
        end = 0
        while end < n:
            while currSum < s and end < n:
                currSum += nums[end]
                end +=1
            
            while currSum >= s and end <= n:
                if (end - start) < minLen:
                    minLen = end - start
                    
                currSum -= nums[start]
                start += 1
        if minLen == n+1:
            minLen = 0
        return minLen
                    
                    
            
