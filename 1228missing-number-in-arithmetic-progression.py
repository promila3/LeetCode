#https://leetcode.com/problems/missing-number-in-arithmetic-progression/
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        length = len(arr)
        if arr[-1] == arr[0]:
            return arr[0]
        range_diff = arr[-1] - arr[0]
        gaps = length 
        diff = range_diff//gaps
        start = arr[0]
        print(start, diff)
        for i in range(1, length):
            start += diff
            print(start, arr[i])
            if start == arr[i]:
                continue
            return start
