# https://leetcode.com/problems/count-largest-group/
# Time n log n , space log n

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashmap = {}
        for i in range(1, n+1):
            key = sum([int(x) for x in str(i)])
            hashmap[key] = hashmap.get(key, 0) + 1
        maxValue = max(hashmap.values())
        count = sum( 1 for v in hashmap.values() if v == maxValue)
        return count
