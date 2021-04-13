#https://leetcode.com/problems/determine-if-string-halves-are-alike/
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        half_n = n //2
        vowels = ["a","e", "i","o","u"]
        s = s.lower()
        sum_left =  sum([s[:half_n].count(v) for v in vowels])
        sum_right=  sum([s[half_n:].count(v) for v in vowels])
        return sum_left == sum_right
