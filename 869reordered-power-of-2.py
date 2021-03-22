# https://leetcode.com/problems/reordered-power-of-2/
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        return any(cand[0] != '0' and bin(int("".join(cand))).count('1') == 1 for cand in itertools.permutations(str(N)))
