# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for a in nums:
            if a in dict1.keys():
                return True
            else :
                dict1[a] = 1
        return False
