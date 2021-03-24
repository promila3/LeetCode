   # https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
   def smallestCommonElement(self, mat: List[List[int]]) -> int:
        histogram = {}
        m = len(mat)
        if m == 0:
            return -1
        n = len(mat[0])
        for row in range(m):
            for col in range(n):
                if mat[row][col] in histogram:
                    histogram[mat[row][col]] +=1
                else :
                    histogram[mat[row][col]] =1
        min_value = math.inf
        print(histogram)
        for item in histogram.items():
            
            if item[1] == m:
                if min_value > item[0]:
                    min_value = item[0]
        if min_value == math.inf:
            min_value = -1
        return min_value
