# https://leetcode.com/problems/merge-two-sorted-lists/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        list3 = ListNode(-1)
        return_result = list3
        while node1 or node2:
            # node1 , node2 both are not null
            if node1 and node2 and node1.val <= node2.val: 
                list3.next = ListNode(node1.val)
                node1 = node1.next
            elif node1 and node2 and node2.val <= node1.val:
                list3.next = ListNode(node2.val)
                node2 = node2.next
            # node1 is not null, node2 is null
            elif node1:
                list3.next = node1
                node1 = node1.next
             # node2 is not null, node1 is null
            elif node2:
                list3.next = node2
                node2 = node2.next
            list3 = list3.next
        return return_result.next