# https://leetcode.com/problems/word-subsets/
class Solution1:
    def wordSubsets1(self, A: List[str], B: List[str]) -> List[str]:
        dictA = {}
        dictB = {}
        def populateDict(word:str):
            for w in word:
                if w in dictA:
                    dictA[w] +=1
                else:
                    dictA[w] =1
        for word in B:
            temp = {}
            for w in word:
                if w in temp:
                    temp[w] +=1
                else:
                    temp[w] =1
            for key in temp:
                if key in dictB:
                    dictB[key] = max(dictB[key], temp[key])
                else:
                    dictB[key] =temp[key]
        result = [] 
        ok = True
        for word in A:
            populateDict(word)
            for key in dictB:
                if key in dictA:
                    if dictA[key] < dictB[key]:
                        ok = False
                        break
                else:
                    ok = False
                    break
            if ok:
                result.append(word)
            ok = True
            dictA = {}
        return result
    
class Solution(object):
    def wordSubsets(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] +=1
            return ans
        
        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i],c)
        ans = []
        for a in A:
            if all(x>=y for x, y in zip(count(a),bmax)):
                ans.append(a)
        return ans
