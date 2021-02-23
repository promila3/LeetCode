# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res=""
        maxLen=0
        for word in d:
            pW=0
            pS=0
            while pW<len(word) and pS<len(s):
                if word[pW]==s[pS]:
                    pW+=1
                    pS+=1
                else:
                    pS+=1
            if pW==len(word): #ie:word found in S
                if len(word)>maxLen or (len(word)==maxLen and word<res): #the reason for the OR is to return the smallest word if both have the same length
                    res=word
                    maxLen=len(word)
                    
        return res
