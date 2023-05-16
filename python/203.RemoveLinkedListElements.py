# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        save_head = head
        prev_node = None
        node = head
        while save_head and node:
            while save_head and save_head.val == val:
                save_head = save_head.next
                node = save_head
            if node and node.val == val:
                prev_node.next = node.next
            elif node:
                prev_node = node
            if node:
                node = node.next
        return save_head