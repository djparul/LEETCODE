# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]: 
        nodeX, nodeB = headA, headB
        myset = set()
        while nodeX or nodeB:
            if nodeX:
                if nodeX in myset:
                    return nodeX
                myset.add(nodeX)
                nodeX = nodeX.next
            if nodeB:
                if nodeB in myset:
                    return nodeB
                myset.add(nodeB)
                nodeB = nodeB.next
        return None