'''
Runtime: 120 ms, faster than 22.54% of Python3 online submissions for Surface Area of 3D Shapes.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Surface Area of 3D Shapes.
https://leetcode.com/problems/surface-area-of-3d-shapes/
'''

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        result = 0
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    result +=2
                    for r, c in ((i+1, j), (i-1, j), (i,j+1), (i, j-1)):
                        if 0 <= r < N and 0<= c < N:
                            diff = grid[r][c]
                        else:
                            diff = 0
                        result += max(grid[i][j] - diff, 0)
        return result
