# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slower, slow, fast = head, head, head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while slower != slow:
                    slower = slower.next
                    slow = slow.next
                return slower
        return None