# https://leetcode.com/problems/longest-palindromic-substring/
def reverse(s): 
    return s[::-1] 

class Solution:
    def longestPalindrome1(self, s: str) -> str:
        maxLen = 0
        maxString = ""
        lenS = len(s)
        if lenS == 1:
            return s
        for i in range(lenS):
            for j in range(lenS, i, -1):
                tResult = self.isPalindrome(s[i:j])
                if tResult:
                    tLen = j - i +1
                    if tLen > maxLen:
                        maxLen = tLen
                        maxString = s[i:j]
                    #break
        return maxString
    
    def isPalindrome(self, s:str) -> bool:
        rev = reverse(s)
        
        if s == rev:
            return True
        else :
            return False
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(s: str, left: int, right:int)->int:
            L, R = left, right
            while (L >= 0 and R < len(s)) and (s[L]== s[R]):
                L -=1
                R +=1
            return R - L -1
        
        if s == None or len(s) <1 :
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i+1)
            lenM = max(len1, len2)
            if lenM > end - start:
                start = i - (lenM -1 )//2
                end = i +  lenM //2
        return s[start:end+1]
        
