# O(n * m) , O(n+m) 
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= part_length and self._check_match(stack, part, part_length):
                for _ in range(part_length):
                    stack.pop()
        return "".join(stack)
    
    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        return "".join(stack[-part_length:]) == part
