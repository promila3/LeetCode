# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath1(self, matrix: List[List[int]]) -> int:
        def dfs(i:int, j:int) -> int:
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            result = 0
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if (0 <= x and x < m and 0 <= y and y < n and matrix[x][y] > matrix[i][j]):
                    result = max(result, dfs(x,y))
                #print(result)
            return result +1
                
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs( i, j))
                #print(result)
        return result
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        def dfs(i:int, j:int) -> int:
            if cache[i][j] != 0 : return cache[i][j]
            dirs = [[0,1],[1,0],[0,-1],[-1,0]]
            result = 0
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if (0 <= x and x < m and 0 <= y and y < n and matrix[x][y] > matrix[i][j]):
                    cache[i][j] = max(cache[i][j], dfs(x,y))
                #print(result)
            cache[i][j] +=1
            return cache[i][j]
                
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        cache = [[0 for i in range(n)] for j in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs( i, j))
                #print(result)
        return result
