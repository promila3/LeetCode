'''
229	
Majority Element II    
33.8%	Medium
Runtime: 116 ms, faster than 93.45% of Python3 online submissions for Majority Element II.
Memory Usage: 13.8 MB, less than 88.24% of Python3 online submissions for Majority Element II.
https://leetcode.com/problems/majority-element-ii/submissions/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        lenNum = len(nums)
        halfFr = math.floor(lenNum /3.0 )
        nums2 = set(nums)
        result = []
        for i in nums2:
            temp = nums.count(i)
            if temp > halfFr:
                result.append(i)
        return result
