#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}
        total = 0
        i = 0
        n = len(s)
        while i < n:
            if i+1 < n and values[s[i] ]< values[s[i+1]]:
                total += values[s[i+1]] - values[s[i]]
                i += 2
            else:
                total += values[s[i]]
                i +=1
        return total
                
