'''
Runtime: 56 ms, faster than 5.50% of Python3 online submissions for Verifying an Alien Dictionary.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Verifying an Alien Dictionary.
'''
# https://leetcode.com/problems/verifying-an-alien-dictionary/

import string
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #Decode
        #sort words after mapping as a
        #and then create  a dictionary with the original words like this
        #if the two dictionaries are the same then correct.
        
        correctSeq =  list(string.ascii_lowercase[0:26])
        orderSeq = list(order)
        print(orderSeq, correctSeq)
        
        newwords = []
        translateDict = {}
        for aWord in words:
            newWord = self.convert(aWord, correctSeq, orderSeq)
            newwords.append(newWord)
            translateDict[newWord] = aWord
        print(newwords)   
        newwords.sort()
        print(newwords)
        result = []
        for aWord in newwords:
            result.append(translateDict[aWord])
        print(result)
        diffResult = self.compare(result,words)
        return diffResult
        
    def convert(self, aWord : str, correctSeq : List[str], orderSeq : List[str]) -> str:
        newWord =''
        for char1 in aWord:
            indexN = orderSeq.index(char1)
            newWord = newWord + correctSeq[indexN]
        
        return newWord

    def compare(self, a: List[str], b : List[str]) -> bool:
        lena = len(a)
        for i in range(lena):
            if a[i] != b[i] :
                return False
        return True
