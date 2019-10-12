'''
Runtime: 56 ms, faster than 6.81% of Python3 online submissions for Most Common Word.
Memory Usage: 13.7 MB, less than 5.88% of Python3 online submissions for Most Common Word.
'''
# https://leetcode.com/problems/most-common-word/submissions/

import re
import operator

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #paragraph = "a, a, a, a, b,b,b,c, c"
        #banned = ["a"]
        #paragraph.translate(str.maketrans('', '', string.punctuation))
        #paragraph.translate(str.maketrans(''.'', string.punctuation))
        #list1 = paragraph.split("[\\s\\-\\.\\'\\?\\,\\_\\@]+")
        list1 = re.sub(r'[^\w\s]',' ',paragraph)
        list1 = list1.strip().split(' ')
        print(list1)
        dict1 = {}
        for a in list1:
            if a == '':
                continue
            temp = a.lower()
            
            if temp in banned:
                continue
            if temp in dict1.keys():
                dict1[temp] +=1
            else :
                dict1[temp] = 1
       
        sorted_d = sorted(dict1.items(), key=operator.itemgetter(1))
        print(sorted_d)
        return sorted_d[-1][0]
        
