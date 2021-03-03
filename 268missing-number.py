#https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = -1
        nums.sort()
        n = len(nums)
        if nums[0] != 0:
            return 0
        for i in range(1, n):
            if nums[i] > nums[i-1] +1 :
                missing = nums[i-1] +1 
        if missing == -1:
            missing = n
        return missing
