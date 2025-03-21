# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/
class Solution:
    
    def minOperations(self, nums: List[int]) -> int:
        def flipper(first: int):
            nums[first] = 1^nums[first] 
            nums[first+1] = 1^nums[first+1]
            nums[first+2] = 1^nums[first+2]

        count = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flipper(i)
                count +=1
        
        if sum(nums) == len(nums):
            return count
        else:
            return -1
