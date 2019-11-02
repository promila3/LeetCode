# https://leetcode.com/problems/n-th-tribonacci-number/submissions/
'''
Runtime: 36 ms, faster than 66.55% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for N-th Tribonacci Number.
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+3)
        dp[0] = 0
        dp[1] = 1
        dp[2]  = 1
        return self.fib(n, dp)
    
    def fib(self, n, dp):
        if n == 0:
            return dp[0]
        if n == 1:
            return dp[1]
        if n == 2:
            return dp[2]
        '''
        if i > n:
            return 0
        if i == n:
            return 1
        '''
        if dp[n]  > 0:
            return dp[n]
        dp[n] = self.fib(n-1, dp) + self.fib(n-2, dp) + self.fib(n-3, dp)
        
        return dp[n]
