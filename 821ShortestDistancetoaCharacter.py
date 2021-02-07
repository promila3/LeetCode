 # https://leetcode.com/problems/shortest-distance-to-a-character/
 class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        n = len(s)
        result = [n for x in s]

        prev = -2 * n
        for i in range(n):
            if s[i] == c:
                prev = i
                result[i] = 0
                continue
            result[i] = i - prev
        prev = 2 * n
        for i in range(n-1,-1,-1):
            if s[i] == c:
                prev = i
                result[i] = 0
                continue
            result[i] = min(result[i], prev - i)
        return result
