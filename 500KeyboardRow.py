'''
Runtime: 28 ms, faster than 63.43% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
https://leetcode.com/problems/keyboard-row/
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        def checkWord(word, row1):
            lenW = len(word)
            temp = sum([1 for x in word if x.upper() in row1])
            #print(temp)
            if temp == lenW:
                #result.append(word)
                return True
            else:
                return False
        row1 = ['Q','W','E','R','T','Y','O','U','I','P']
        row2 = ['A','S','D','F','G','H','J','K','L']
        row3 = ['Z','X','C','V','B','N','M']
        result = []
        for word in words:
            lenW = len(word)
            temp= checkWord(word, row1)
            if temp:
                result.append(word)
                continue
            temp= checkWord(word, row2)
            if temp:
                result.append(word)
                continue
            temp= checkWord(word, row3)
            if temp:
                result.append(word)
        return result
        
