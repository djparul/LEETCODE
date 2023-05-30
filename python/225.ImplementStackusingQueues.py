# 225.ImplementStackusingQueues.py
# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
        self.queue1 = [] #final queue
        self.queue2 = [] #extra queue

    def push(self, x: int) -> None:
        while self.queue1:
            self.queue2.append(self.queue1.pop())
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.pop())

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()