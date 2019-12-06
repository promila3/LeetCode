'''

Runtime: 752 ms, faster than 8.16% of Python3 online submissions for Sliding Window Maximum.
Memory Usage: 19.4 MB, less than 92.31% of Python3 online submissions for Sliding Window Maximum.

'''
# https://leetcode.com/problems/sliding-window-maximum/

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lenNums = len(nums)
        if lenNums == 0:
            return []
        
        first = nums[0]
        last = nums[k-1]
        maxSum = max(nums[0:k])
        result = [maxSum]
        for i in range(1,lenNums-k+1):
            tempSum = max(nums[i:k+i])
            #if result[i-1] < tempSum:
            result.append(tempSum)
            #else:
             #   result.append(result[i-1])
        return result
        
