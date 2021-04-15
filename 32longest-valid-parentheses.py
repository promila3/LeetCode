#https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses2(self, s: str) -> int:
        maxlen = 0
        for i in range(len(s)):
            for j in range(i+2, len(s) +1, 2):
                if self.is_valid(s[i:j]):
                    maxlen = max(maxlen, j-i)
        return maxlen
    
    def is_valid(self, s:str)->bool:
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            elif len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
            
        return len(stack) == 0
    
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = (dp[i-2] if i >=2 else 0 )+2
                elif (i - dp[i-1]) >0 and s[i-dp[i-1]-1] == "(":
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if ( i-dp[i-1]) >=2 else 0 ) +2
                maxans = max(maxans, dp[i])
        return maxans
