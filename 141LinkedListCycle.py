# 141 Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/submissions/
'''
Runtime: 52 ms, faster than 83.03% of Python3 online submissions for Linked List Cycle.
Memory Usage: 16.4 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashSet = set()
        pos = -1
        currentPos = -1
        current = head
        while current :
            if current in  hashSet:
                currentPos += 1
                return True
            hashSet.add(current)
            current = current.next
            currentPos +=1
        return False
