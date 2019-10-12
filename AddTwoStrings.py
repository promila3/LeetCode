'''
Runtime: 32 ms, faster than 99.29% of Python3 online submissions for Add Strings.
Memory Usage: 13.6 MB, less than 11.11% of Python3 online submissions for Add Strings.
Next challenges:
'''
https://leetcode.com/problems/daily-temperatures/submissions/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = int(num1) + int(num2)
        return str(result)
