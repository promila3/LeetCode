'''
Runtime: 24 ms, faster than 98.87% of Python3 online submissions for Add Binary.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Add Binary.
'''
#https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = self.convert(a)
        a2 = self.convert(b)
        print(a1, a2)
        result = self.convertB(a1+a2)
        return result
    
    def convert(self, a:str) -> int:
        lena = len(a)
        result = 0
        for i in range(lena-1, -1, -1):
            result += int(a[(lena-1) -i]) * (2 ** i)
        return result
    
    def convertB(self, a:int) -> str:
        result =''
        q = a 
        while q :
            remainder = q % 2
            result = str(remainder) + result
            q = q // 2
        if len(result) == 0:
            return "0"
        return result
        
