#https://leetcode.com/submissions/detail/262916106/
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        q = []
        numS = list(set(nums))
        lenL = len(numS)
        if len(numS) < 3 :
            return max(numS)
        elif len(numS) == 3:
            return min(numS)
        
        q = [numS[0],numS[1], numS[2]]
        for i in range(3, lenL):
            temp = min(q)
            if numS[i] > temp:
                q.remove(temp)
                q.append(numS[i])
                
        return min(q)
