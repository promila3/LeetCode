#https://leetcode.com/problems/beautiful-arrangement-ii/
class Solution:
    def constructArray1(self, n: int, k: int) -> List[int]:
        seen = [False] * n
        def num_uniq_diffs(arr):
            ans = 0
            for i in range(n):
                seen[i] = False
            for i in range(len(arr) -1):
                delta = abs(arr[i] - arr[i+1])
                if not seen[delta]:
                    ans +=1
                    seen[delta] = True
            return ans
        
        for cand in itertools.permutations(range(1,n+1)):
            if num_uniq_diffs(cand) == k:
                return cand
            
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1, n-k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n-k + i//2)
            else:
                ans.append(n - i//2)
        return ans
