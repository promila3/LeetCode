# https://leetcode.com/problems/sort-array-by-increasing-frequency/description/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))

    def frequencySort(self, nums: List[int]) -> List[int]:
        count: List[int] = [ 0 for _ in range(201)]
        for num in nums:
            count[num + 100] +=1
        nums.sort(key=lambda val: (count[val+100], -val))
        return nums
