# 622.DesignCircularQueue.py
# https://leetcode.com/problems/design-circular-queue
class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.space_left = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
        # We initialized doubly linked list with dummy nodes

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr_node = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr_node
        self.right.prev = curr_node
        self. space_left -= 1
        return True
 
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self. space_left += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space_left == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()