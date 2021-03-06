#https://leetcode.com/problems/next-permutation/
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def reverse(start:int):
            i = start
            j = n - 1
            while (i <j):
                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
        i = n-2
        while i>=0 and nums[i+1] <= nums[i]:
            i -=1
        if i >= 0:
            j = n-1
            while j >= 0 and nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]
        reverse(i+1)
