# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recurrsive_reverse(self, node, prev = None):
        if node is None:
            return prev
        n = node.next
        # curr = node
        node.next = prev
        return self.recurrsive_reverse(n, node)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurrsive_reverse(head)