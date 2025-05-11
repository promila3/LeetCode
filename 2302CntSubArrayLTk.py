# https://leetcode.com/problems/count-subarrays-with-score-less-than-k
'''
Let n be the length of the nums.

Time complexity: O(n).
We only need to traverse the array once.

Space complexity: O(1).
'''
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res, total = 0, 0
        i = 0
        for j in range(n):
            total += nums[j]
            while i <= j and total * (j - i +1) >= k:
                total -= nums[i]
                i +=1
            res += j - i +1
        return res
