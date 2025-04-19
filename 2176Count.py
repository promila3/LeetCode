# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/?envType=daily-question&envId=2025-04-17
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        indices = defaultdict(list)
        for curr, num in enumerate(nums):
            for prev in indices[num]:
                if prev*curr % k == 0:
                    pairs += 1
            indices[num].append(curr)
        return pairs
