'''
Runtime: 164 ms, faster than 46.89% of Python3 online submissions for Find Pivot Index.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Find Pivot Index.
https://leetcode.com/problems/find-pivot-index/submissions/
'''

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prev = 0
        left = 0 
        right = 0
        total = sum(nums)
        right = total
        lenN = len(nums)
        for i in range(lenN):
            left += prev
            right = right - nums[i]
            #total = total - nums[i]
            prev = nums[i]
            if left  == right:
                return i
        return -1
