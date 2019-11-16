'''
Runtime: 32 ms, faster than 90.47% of Python3 online submissions for House Robber.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for House Robber.
'''
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        sum1 = 0
        lenNums = len(nums)
        res = [0 for x in nums]
        if lenNums == 0:
            return sum1
        if lenNums == 1:
            return nums[0]
        res[0] = nums[0]
        if nums[1] > nums[0]:
            res[1] = nums[1]
        else :
            res[1] = nums[0]

        for i in range(2, lenNums):
            res[i] = max(res[i-2]+nums[i], res[i-1])
        return res[lenNums-1]        
