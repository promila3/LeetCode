# https://leetcode.com/problems/count-of-interesting-subarrays

'''
Let n be the length of the nums.

Time complexity: O(n).
We only need to traverse the array once, and the time required is O(n).

Space complexity: O(min(n,modulo))
It is necessary to use a hash map to store the frequency of each element's modulo result in the array. There can be at most O(min(n,modulo)) different modulo results, so the required space is O(min(n,modulo)).
'''
class Solution:
    def countInterestingSubarrays(
        self, nums: List[int], modulo: int, k: int
    ) -> int:
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res
