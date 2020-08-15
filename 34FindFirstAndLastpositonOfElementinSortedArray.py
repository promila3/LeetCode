# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(arr, low, high, x)->int: 
            if high >= low: 
                mid = (high + low) // 2
                if arr[mid] == x: 
                    return mid 
                elif arr[mid] > x: 
                    return binary_search(arr, low, mid - 1, x) 
                else: 
                    return binary_search(arr, mid + 1, high, x) 
            else: 
                return -1
        
        def firstLast()->List[int]:
            lenN = len(nums)
            i = pos
            while i >= 0 and nums[i] == target:
                i -=1
            lower = i+1
            i = pos
            while i < lenN and nums[i] == target:
                i +=1
            higher = i -1
            return [lower, higher]
        
        pos = binary_search(nums, 0, len(nums)-1, target)
        if pos == -1:
            return [-1, -1]
        return firstLast()
