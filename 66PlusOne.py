# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
# O(n) time, O(1) space
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n -1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            
            else :
                digits[idx] +=1
                return digits
        
        return [1] + digits
