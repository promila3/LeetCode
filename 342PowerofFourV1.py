https://leetcode.com/problems/power-of-four/
'''
Runtime: 28 ms, faster than 88.51% of Python3 online submissions for Power of Four.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Power of Four.
'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
      
        while num > 0:
            if num == 1:
                return True
            if num % 4 != 0:
                return False
            else :
                num = num/4
        return False
        
