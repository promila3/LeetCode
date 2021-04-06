#https://leetcode.com/problems/minimum-operations-to-make-array-equal/
class Solution:
    def minOperations(self, n: int) -> int:
        arr = [2*i+1 for i in range(n)]
        average = (arr[0] + arr[-1])//2
        return sum([abs(i-average) for i in arr])//2
