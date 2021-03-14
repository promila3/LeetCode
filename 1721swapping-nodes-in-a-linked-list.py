# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        list_length = 0
        current = head
        while current:
            list_length +=1
            current = current.next
            
        front_node = head
        for i in range(k-1):
            front_node = front_node.next
        end_node = head
        for i in range(list_length -k):
            end_node = end_node.next
        front_node.val, end_node.val = end_node.val, front_node.val
        return head
