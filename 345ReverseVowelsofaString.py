#Runtime: 44 ms, faster than 92.02% of Python3 online submissions for Reverse Vowels of a String.Memory Usage: 15.4 MB, less than 6.67% of Python3 online submissions for Reverse Vowels of a String.class Solution:
  # https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/ 
    def reverseVowels(self, s: str) -> str:
        indexLst = []
        vow = []
        lenS = len(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        if lenS == 0:
            return s
        for i in range(lenS):
            if s[i] in vowels:
                indexLst.append(i)
                vow.append(s[i])
        vow = vow[::-1]

        result = []
        j = 0
        '''
        for i in range(lenS):
            if i in indexLst:
                result.append(vow[j])
                j +=1
            else:
                result.append(s[i])
        '''
        result = list(s)
        for vw in vow:
            result[indexLst[j]] = vw
            j +=1
            
        return ''.join(result)
        
