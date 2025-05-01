# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n-1):
            if nums[i] == (nums[i-1] + nums[i+1]) * 2:
                ans +=1
        return ans
