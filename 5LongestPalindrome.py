'''
Runtime: 9040 ms, faster than 5.03% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
'''
# https://leetcode.com/problems/longest-palindromic-substring/
def reverse(s): 
    return s[::-1] 

class Solution:
    def longestPalindrome(self, s: str) -> str:
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
