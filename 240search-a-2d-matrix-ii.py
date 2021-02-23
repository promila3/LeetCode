# https://leetcode.com/problems/search-a-2d-matrix-ii/
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row:int)-> bool:
            low = 0
            high = n-1
            while high >= low:
                mid = (low + high)//2
                if matrix[row][mid] < target:
                    low = mid +1
                elif matrix[row][mid] > target:
                    high = mid - 1
                else:
                    return True
            return False
        if not matrix:
            return False
        n = len(matrix[0])
        m = len(matrix)
        for i in range(m):
            if binary_search(i):
                return True
        return False
        
                    
