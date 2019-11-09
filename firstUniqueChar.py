'''
Runtime: 100 ms, faster than 84.93% of Python3 online submissions for First Unique Character in a String.Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Unique Character in a String.
'''
# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        queue = []
        dict1 = {}
        dictSingle = {}
        lenS = len(s)
        for i in range(lenS):
            a = s[i]
            if a in queue:
                queue.remove(a)
                dictSingle.pop(a)
                dict1[a] = 2
            elif a in dict1:
                pass
            else:
                queue.append(a)
                dictSingle[a] = i
                
        if len(queue) == 0:
            return -1
        else:
            return dictSingle[queue[0]]
                
                
        
