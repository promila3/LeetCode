#https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if (i - coin) < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] +1)
        return -1 if dp[amount] > amount else dp[amount]
        
        
