# https://leetcode.com/submissions/detail/262903786/
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        lenL = len(nums)
        result = True
        swap = False
        #print lenL
        point = -1
        for i in range(lenL-1):
            #print nums, i
            if nums[i+1] >= nums[i] :
                #print nums , i, swap
                pass
            elif swap:
                result = False
                return result
            else :
                swap = True
                point = i 
                
                #print nums , i, swap
                
        
        if (point != -1) and (lenL-1 > point+1) and nums[point +2]  < nums[point] :
            nums[point] = nums[point+1]
        elif point != -1  and lenL-1 > point:
            nums[point+1] = nums[point]
        for i in range(lenL-1):
            #print nums, i
            if nums[i+1] < nums[i] :
                #print nums , i, swap
                result = False
                return result
        #print point, nums
        return result
