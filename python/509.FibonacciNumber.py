# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        if(n > 1):
            return (self.fib(n-1) + self.fib(n-2))
        if (n <= 1):
            return n