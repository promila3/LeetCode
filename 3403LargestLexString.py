# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        len_possible = len(word) - numFriends + 1
        result = ""
        for i in range(len(word) - len_possible + 1):
            temp = word[i:i+len_possible]
            if temp > result:
                result = temp
        
        
        if numFriends != 1:
            for i in range(len_possible):
                temp = word[len(word)-len_possible+i:]
                #print(temp)
                if temp > result:
                    result = temp
        
        return result
