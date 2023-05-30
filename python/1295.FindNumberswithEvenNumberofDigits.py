# 1295.FindNumberswithEvenNumberofDigits.py
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
            # count = 0
            # while i > 0:
            #     count += 1
            #     i = i // 10
            # if count % 2 == 0:
            #     res += 1
        return res