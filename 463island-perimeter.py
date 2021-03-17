#https://leetcode.com/problems/island-perimeter/
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def checkNeighbours(row, col):
            result = 0
            for i, j in ([0,1],[1,0],[0,-1],[-1,0]):
                current_row = row + i
                current_col = col + j
                if 0 <= current_row and current_row < rows:
                    if 0 <= current_col and current_col < cols:
                        result += 0 if grid[current_row][current_col] == 1 else 1
                    else:
                        result +=1
                else :
                    result +=1
            return result
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        perimeter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    perimeter += checkNeighbours(row, col)
        return perimeter
