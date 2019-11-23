#https://leetcode.com/problems/valid-anagram/
'''
Runtime: 44 ms, faster than 90.85% of Python3 online submissions for Valid Anagram.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Valid Anagram.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for letter in s:
            if letter in dict1:
                dict1[letter] += 1
            else :
                dict1[letter] = 1
        
        for letter in t:
            if letter in dict1:
                dict1[letter] -= 1
                if dict1[letter] < 0:
                    return False
            else :
                return False
        
        for letter in dict1:
            if dict1[letter] != 0:
                return False
            
        return True
