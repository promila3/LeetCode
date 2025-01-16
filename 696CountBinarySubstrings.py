# https://leetcode.com/problems/count-binary-substrings/description/
class Solution:
    def countBinarySubstrings1(self, s: str) -> int:
        groups =[1]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                groups[-1] +=1
            else:
                groups.append(1)
        
        result = 0
        for i in range(1, len(groups)):
            result += min(groups[i], groups[i-1])
        return result
    def countBinarySubstrings(self, s: str) -> int:
        result, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur +=1 
            else:
                result += min(prev, cur)
                prev, cur = cur, 1
        return result + min(prev, cur)
