# https://leetcode.com/problems/student-attendance-record-i/
'''
Runtime: 28 ms, faster than 63.43% of Python3 online submissions for Keyboard Row.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Keyboard Row.
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        lenS = len(s)
        if lenS == 0:
            return False
        prev = s[0]
        ctA = 0
        ctL = 0
        if prev == "L" :
            ctL +=1
        elif prev == "A":
            ctA +=1
            prev = "-"
        else :
            prev = "-"
            
        for i in range(1, lenS):
            if s[i] == prev:
                ctL +=1
                if ctL >= 3 :
                    return False
                prev = s[i]
            else:
                if s[i] == "L":
                    ctL = 1
                    prev = s[i]
                elif s[i] == "A":
                    ctL = 0
                    ctA +=1 
                    if ctA >= 2:
                        return False
                    prev = "-"
                else:
                    ctL = 0
                    prev = "-"
            print(ctA,ctL, i)
            
        return True
                
        
        
