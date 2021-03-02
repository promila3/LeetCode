
# https://leetcode.com/problems/distribute-candies/
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ctype = set(candyType)
        types = len(ctype)
        n = len(candyType)
        result = n //2
        if result > types:
            result = types
        return result
