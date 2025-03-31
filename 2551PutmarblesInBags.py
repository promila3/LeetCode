# https://leetcode.com/problems/put-marbles-in-bags/?envType=daily-question&envId=2025-03-31
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairweights = [weights[i]+weights[i+1] for i in range(n-1)]

        pairweights.sort()

        answer = 0
        for  i in range(k-1):
            answer += pairweights[n-2-i] -pairweights[i]

        return answer
