    # https://leetcode.com/problems/longest-harmonious-subsequence/
    def findLHS(self, nums: List[int]) -> int:
        xset = set(nums)
        if len(xset) == 1:
            return 0
        if len(xset) == 2:
            return len(nums)
        counts = [[nums.count(x), x] for x in xset ]
        #counts.sort(reverse=True)
        counts.sort(key = lambda x: x[1]) 
        #modes = [counts[0][1], counts[1][1]]
        print(counts)
        maxlen = 0
        temp = 0
        '''
        for x in nums:
            if x in modes:
                temp+=1
        return temp
        '''
        for i in range(len(counts)-1):
            if counts[i+1][1] - counts[i][1] == 1:
                maxlen = max(maxlen,counts[i+1][0] + counts[i][0] )
        return maxlen
