#https://leetcode.com/submissions/detail/265034272/
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        result1, result2 = True, True
        lenA = len(A)
        for i in range(lenA-1):
            if A[i] <= A[i+1]:
                continue
            else:
                result1 = False
                break
        for i in range(lenA-1):
            if A[i] >= A[i+1]:
                continue
            else:
                result2 = False
                break  
        return (result1 or result2)
