#https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup = -1
        missing = 1
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1] +1:
                missing = nums[i-1] +1
        
        if nums[n-1] != n : missing = n
        else: pass
        
        return [dup, missing]
