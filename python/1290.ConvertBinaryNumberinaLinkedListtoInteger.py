# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        length = decimal_val = 0
        while node:
            length += 1
            node = node.next
        while head:
            decimal_val += head.val * math.pow(2,length-1)
            head = head.next
            length -= 1
        return int(decimal_val)