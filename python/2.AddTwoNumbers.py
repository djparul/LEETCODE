# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_node = ListNode(18)
        res_head = cur_node
        my_sum = 0
        my_carry = 0
        while l1 or l2:
            
            if l1 and l2:
                my_sum = l1.val + l2.val + my_carry
                l1, l2 = l1.next, l2.next
            elif l1:
                my_sum = l1.val + my_carry
                l1 = l1.next
            elif l2:
                my_sum = l2.val + my_carry
                l2 = l2.next

            my_carry = int(my_sum / 10)
            cur_node.next = ListNode(my_sum % 10)
            cur_node = cur_node.next

        if (my_carry != 0):
            cur_node.next = ListNode(1)
        return res_head.next