'''
Runtime: 596 ms, faster than 7.21% of Python3 online submissions for Most Profit Assigning Work.
Memory Usage: 15.5 MB, less than 75.00% of Python3 online submissions for Most Profit Assigning Work.
https://leetcode.com/problems/most-profit-assigning-work/
'''
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        result = 0
        z = list(zip(difficulty, profit))
        z.sort()
        print(z)
        maxProfit, maxProfits = 0, []
        for _, gain in z:
            maxProfit = max(maxProfit, gain)
            maxProfits.append(maxProfit)
        for w in worker:
            wProfit = 0
            i = 0
            lenP = len(profit)
            
            idx = self.uppperBsearch(z, w) - 1
            '''
            while i < lenP and  w >= z[i][0]: #w >= difficulty[i] :
                wProfit = max(wProfit, z[i][1])
                i +=1
            '''
            #wProfit = 0
            if idx > -1:
               # wProfit = z[idx][1]
                result += maxProfits[idx]
            
        return result
    
    def uppperBsearch(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right)//2
            if target >= arr[mid][0]:
                left = mid + 1
            else:
                right = mid
        return right
        
