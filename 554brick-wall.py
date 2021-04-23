# https://leetcode.com/problems/brick-wall/
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        sum_map = {}
        for row in wall:
            row_sum = 0
            for i in range(len(row)-1):
                row_sum += row[i]
                if row_sum in sum_map:
                    sum_map[row_sum] +=1
                else:
                    sum_map[row_sum] =1
        result = len(wall)
        for temp_sum in sum_map:
            result = min(result, len(wall) - sum_map[temp_sum])
        return result
