'''
Runtime: 36 ms, faster than 74.83% of Python3 online submissions for Happy Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Happy Number.
'''
#https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        prevNum = -1
        prevSet = set([2])
        while n != prevNum and n not in prevSet:
            prevSet.add(n)
            digits = self.getDigits(n)
            print(digits)
            sumSqr = self.getSumSqr(digits)
            if sumSqr == 1 :
                return True
            prevNum = n
            n = sumSqr
        return False
    def getDigits(self, n: int)-> list:
        result = []
        rem = n
        if rem == 0:
            return [0]
        while rem:
            
            q = rem % 10
            rem = rem // 10
            result.append(q)
        return result
    
    def getSumSqr(self, digits: list)-> int:
        result = 0
        for d in digits:
            result += d**2
        return result
