# O(n) and O(n)
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
class Solution:
    def minLength(self, s: str) -> int:
        stack  = []

        for current_char in s:
            if not stack:
                stack.append(current_char)
                continue
            if current_char == "B" and stack[-1] == "A":
                stack.pop()
            elif current_char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(current_char)
        
        return len(stack)
