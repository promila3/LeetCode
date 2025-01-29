# O(n) and O(n)
# 12 ms compared to 140 ms when I did in 2019. great !
# https://leetcode.com/problems/contains-duplicate-ii/
# 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i in range(len(nums)):
            if nums[i] in index_map:
                if abs(i-index_map[nums[i]]) <= k:
                    return True
                else :
                    index_map[nums[i]] = i
            else :
                index_map[nums[i]] = i
        return False
