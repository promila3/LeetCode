# https://leetcode.com/problems/merge-strings-alternately/description/
# O(n) , O(n)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        result = ""
        i = 0
        j = 0
        while (len1 > 0 and len2 > 0):
            result += word1[i] + word2[j]
            i+=1
            j+=1
            len1 -=1
            len2 -=1
        while (len1 > 0):
            result += word1[i]
            i+=1
            len1 -=1
        while (len2 > 0):
            result += word2[j]
            j +=1
            len2 -=1
        return result
