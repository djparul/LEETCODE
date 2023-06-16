# 1800.MaximumAscendingSubarraySum.py
# https://leetcode.com/problems/maximum-ascending-subarray-sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = 0
        for i, val in enumerate(nums[1:]):
            if val <= nums[i]:
                max_sum = max(max_sum, cur_sum)
                cur_sum = val
            else:
                cur_sum += val
        return max(max_sum, cur_sum)