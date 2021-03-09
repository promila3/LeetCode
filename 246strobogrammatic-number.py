#https://leetcode.com/problems/strobogrammatic-number/
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        #sb_numbers = [0,1,8,6,9]
        sb_dict = {0:0, 1:1, 8:8, 6:9, 9:6}
        str_num = str(num)
        new_num = ""
        for ch in str_num:
            if int(ch) not in sb_dict:
                return False
            new_num += str(sb_dict[int(ch)])
        print(new_num[::-1])
        return num == new_num[::-1]
