#https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
class Solution:
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        n = len(nums)
        first = -1
        last = -1
        i = 0
        while i < n-1:
            if nums[i] > nums[i+1]:
                if first == -1:
                    first = i
                    last = i +1
                    previous = nums[i+1]
                    i +=1 
                    if i < n-1:
                        while i < n-1 and nums[i] == nums[i+1]:
                            last = i +1
                            i +=1
                                                         
                    continue
                last = i+1
                i +=1
                if i < n-1:
                    while i < n-1 and nums[i] == nums[i+1]:
                        last  = i+1 
                        i +=1
                        
                continue
            i+=1
                
        if first == -1:
            return 0
        return last - first +1
    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        n = len(nums)
        l = n
        r = 0
        for i in range(n-1):
            for j in range(i, n):
                if nums[i] > nums[j]:
                    l = min(l, i)
                    r = max(j, r)
        return 0 if r - l < 0 else r -l+1
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        clone = nums[:]
        clone.sort()
        n = len(nums)
        l = n
        r = 0
        for i in range(n):
            if nums[i] != clone[i]:
                l = min(l, i)
                r = max(i, r)
        return 0 if r - l < 0 else r -l+1
