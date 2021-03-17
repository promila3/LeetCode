# https://leetcode.com/problems/construct-binary-tree-from-string/ 
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree1(self, s: str) -> TreeNode:
        if s == None:
            return None
        root_str = ''
        i = 0
        print(s)
        for c in s:
            if c != '(':
                root_str += c
                i +=1
            elif c == '(':
                #i+=1
                break
        print(root_str)
        head = TreeNode(int(root_str))
        print(s[i])
        if s[i] != '(':
            return head
        start_left = i +1
        end_left = s.find(')',i, len(s))
        left_str = s[i:end_left+1]
        head.left = self.str2tree(left_str)
        if end_left +1 == len(s):
            return head
        start_right  = end_left +2
        end_right = s.find(')',start_right, len(s))
        right_str = s[end_left+1:end_right+1]
        head.right = str2tree(self, right_str)
        return head
    def str2tree(self, s: str) -> TreeNode:
        return self._str2treeInternal(s, 0)[0]
    def _getNumber(self, s:str, index:int)-> (int, int):
        is_negative = False
        if s[index] == '-':
            is_negative = True
            index +=1
        
        number = 0
        while index <len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index +=1
            
        return number if not is_negative else -number, index
    
    def _str2treeInternal(self, s:str, index:int)->(TreeNode, int):
        if index == len(s):
            return None, index
        
        value, index = self._getNumber(s, index)
        node = TreeNode(value)
        
        if index < len(s) and s[index] == '(':
            node.left, index = self._str2treeInternal(s, index+1)
            
        if node.left and index < len(s) and s[index] == '(':
            node.right, index = self._str2treeInternal(s, index +1)
            
        return node, index +1 if index < len(s) and s[index] == ')' else index
