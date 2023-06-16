# 1979.FindGreatestCommonDivisorofArray.py
# https://leetcode.com/problems/find-greatest-common-divisor-of-array
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small_num = min(nums)
        large_num = max(nums)
        res = 1
        for i in range(2, large_num + 1):
            if large_num % i == 0 and small_num % i == 0:
                res = i
        return res