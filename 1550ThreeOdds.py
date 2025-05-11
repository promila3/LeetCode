@ https://leetcode.com/problems/three-consecutive-odds/description/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        three_odds = 0
        for num in arr:
            if num % 2  == 1:
                three_odds +=1
            else:
                three_odds = 0
            
            if three_odds == 3:
                return True
        
        return False
