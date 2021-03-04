#https://leetcode.com/problems/longest-substring-without-repeating-c/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        setChars = set()
        result = 0
        s = list(s)
        i, j = 0, 0
        while i < n and j < n:
            if s[j] not in setChars:
                setChars.add(s[j])
                j+=1
                result = max(result, j -i)
            else:
                setChars.remove(s[i])
                i+=1
        return result
