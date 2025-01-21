# https://leetcode.com/problems/crawler-log-folder/description/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        folder_depth = 0

        for current_op in logs:
            if current_op == "../":
                folder_depth = max(0, folder_depth -1)
            elif current_op != "./":
                folder_depth +=1
        
        return folder_depth
