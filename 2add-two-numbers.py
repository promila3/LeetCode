# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#https://leetcode.com/problems/add-two-numbers/
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(-1)
        head = result
        carry = 0
        while l1 != None or l2 != None:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
            if l2 :
                val2 = l2.val
            tempSum = val1+ val2 + carry
            print(tempSum)
            carry = 0
            rem = tempSum % 10
            quot = tempSum // 10
            carry = quot
            
            result.next = ListNode(rem)
            result = result.next
            print(result.val)
            if l1 and l1.next:
                l1 = l1.next
            else:
                l1 = None
            if l2 and l2.next:
                l2 = l2.next
            else:
                l2 = None
            
        if carry:
            result.next = ListNode(carry)
        return head.next
            
        
