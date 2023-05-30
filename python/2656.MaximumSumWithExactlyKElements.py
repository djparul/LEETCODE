# 2656.MaximumSumWithExactlyKElements.py
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = nums[-1]
        res = 0
        for i in range(k):
            res += count
            count += 1
        return res