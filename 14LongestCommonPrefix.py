#https://leetcode.com/problems/longest-common-prefix/# 
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_short = float('inf')
        index_short = -1
        for i in range(len(strs)):
            if len_short > len(strs[i]):
                len_short = len(strs[i])
                index_short = i
        
        prefix = ""
        for i in range(len_short):
            tmp_prefix = strs[index_short][i]
            found = True
            for j in range(len(strs)):
                if found :
                    if index_short != j :
                        if strs[j][i] != tmp_prefix:
                            found = False
            if found:
                prefix = prefix + tmp_prefix
            else :
                break
        
        return prefix
