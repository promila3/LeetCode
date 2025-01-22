# O(n), O(n)
# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]":"["}

        for chr in s:
            if chr in mapping:
                top = stack.pop() if stack else "*"

                if mapping[chr] != top:
                    return False
            else:
               stack.append(chr)
        return not stack 
