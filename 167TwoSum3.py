# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
Runtime: 68 ms, faster than 75.54% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Two Sum II - Input array is sorted.
''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lenL = len(numbers)
        i = 0
        j = lenL-1
        while (i < j ):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
                
