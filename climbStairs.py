'''
https://leetcode.com/problems/climbing-stairs/
Runtime: 52 ms, faster than 6.08% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
Next challenges:
'''
class Solution:
    def fib(self, i, n, dp):
        if n == 0:
            return 0
        if i > n:
            return 0
        if i == n:
            return 1
        if dp[i+1] == 0:
            dp[i+1] = self.fib(i+1,n, dp)
        if dp[i+2] == 0:
            dp[i+2] = self.fib(i+2, n, dp)    
        return dp[i+1] + dp[i+2]
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+2)
        return self.fib(0,n, dp)
