'''
Runtime: 204 ms, faster than 12.13% of Python3 online submissions for Max Area of Island.
Memory Usage: 16.7 MB, less than 9.09% of Python3 online submissions for Max Area of Island.
https://leetcode.com/problems/max-area-of-island/
'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N = len(grid) 
        if N == 0:
            return 0
        M = len(grid[0])
        gridcpy = [[False for x in range(M)] for y in range(N)]
        
        def dfs(r:int, c:int) -> int:
            gridcpy[r][c] = True
            temp2 = 0
            for nr, nc in ((r+1,c),(r-1,c), (r,c+1),(r,c-1)):
                print(nr,nc)
                if 0<=nr < N and 0 <= nc < M:
                    if not gridcpy[nr][nc] and grid[nr][nc]:
                        temp2 += dfs(nr, nc) +1
            return temp2
                        

        print(gridcpy)
        result = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] and not gridcpy[i][j]:
                    #gridcpy[i][j] = True
                    temp = dfs(i,j) +1
                    print(temp)
                    result = max(temp, result)
        return result
                
