# https://leetcode.com/problems/merge-two-sorted-lists/ 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-200)
        head = result
        while list1 != None and list2 != None:
            if list1.val < list2.val :
                result.next = list1
                list1 = list1.next
            else :
                result.next = list2
                list2 = list2.next
            result = result.next
        
        if list1 :
            result.next = list1
            
        if  list2 :
            result.next = list2
            
        return head.next
            
