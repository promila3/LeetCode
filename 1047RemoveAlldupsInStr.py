# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
# O(n), O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        len_s = len(s)

        for i in range(len_s):
            if len(stack) > 0:
                if stack[-1] == s[i]:
                    stack.pop()
                    continue
                else :
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return "".join(stack)
