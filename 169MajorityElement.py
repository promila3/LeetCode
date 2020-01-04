'''
169	
Majority Element    
55.3%	Easy
Runtime: 164 ms, faster than 98.11% of Python3 online submissions for Majority Element.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Majority Element.
https://leetcode.com/problems/majority-element/submissions/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lenNum = len(nums)
        halfFr = math.floor(lenNum /2.0 )
        nums2 = set(nums)
        for i in nums2:
            temp = nums.count(i)
            if temp > halfFr:
                return i
