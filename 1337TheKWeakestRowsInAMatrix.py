#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        for i, row in enumerate(mat):
            counts.append([row.count(1),i])
        counts.sort()
        result = []
        for i in range(k):
            result.append(counts[i][1])
        return result
