# https://leetcode.com/problems/ones-and-zeroes/
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[ 0 for x in range(n+1)] for y in  range(m+1)]
        for s in strs:
            ctr = [s.count('0'), s.count('1')]
            for zeros in range(m, ctr[0]-1, -1):
                for ones in range(n, ctr[1] -1, -1):
                    dp[zeros][ones] = max(1+dp[zeros-ctr[0]][ones-ctr[1]], dp[zeros][ones])
        return dp[m][n]
