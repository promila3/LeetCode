# 2206 https://leetcode.com/problems/divide-array-into-equal-pairs/?envType=daily-question&envId=2025-03-17
# O(n) and O(1)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        temp = [0] * (500+1)
        #print(nums)
        #print(len(temp))
        for num in nums:
            temp[num] +=1
        
        for count in temp:
            if count % 2 == 0 :
                continue
            else:
                return False
        
        return True
