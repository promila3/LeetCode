# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid1(self, s: str) -> str:
        result = ""
        stack =[]
        for letter in s:
            if letter == "(":
                stack.append(letter)
            elif letter ==")":
                tempResult =")"
                while len(stack) > 0 and stack[-1] != "(":
                    sLetter = stack.pop()
                    tempResult = sLetter + tempResult
                if len(stack) == 0 and tempResult[0] != "(":
                    tempResult = tempResult[:len(tempResult-1)]
                elif len(stack) == 0:
                    result += tempResult
            else :
                stack.append(letter)
                
        
        while len(stack) > 0:
            letter = stack.pop()
            if letter != "(":
                result = letter + result
                
        return result
        
    def minRemoveToMakeValid(self, s:str)-> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)
