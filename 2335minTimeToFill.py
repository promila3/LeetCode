# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups
'''
Time complexity: O(1) because sorting a fixed-size array of three elements is constant time, as are the addition and maximum operations.
Space complexity: O(1) as we only use a constant amount of additional space.
'''
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        amount.sort()
        total_sum = sum(amount)
        return max(amount[2], (total_sum +1)//2)
    
           
