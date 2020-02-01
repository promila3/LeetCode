'''
Runtime: 440 ms, faster than 64.37% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

Memory Usage: 18.8 MB, less than 100.00% of Python3 online submissions for Find the Smallest Divisor Given a Threshold.
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def lessThan(mid: int) -> bool:
            return (sum(x//mid if x%mid == 0 else x//mid+1 for x in nums) <= threshold)
        left, right = 1, max(nums)
        while left<right:
            mid = (left+right)//2
            if lessThan(mid):
                right = mid
            else:
                left = mid +1
        return left
            
