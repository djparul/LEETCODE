# 2652.SumMultiples.py
# https://leetcode.com/problems/sum-multiples
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            if i % 3 == 0:
                count += i
            elif i % 5 == 0:
                count += i
            elif i % 7 == 0:
                count += i
            else:
                pass
        return count