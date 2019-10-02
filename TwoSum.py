# https://leetcode.com/submissions/detail/262315839/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numLen = len(nums)
        for i in range(numLen-1):
            for j in range(i+1,numLen):
                if nums[i] + nums[j] == target :
                    return [i, j]
