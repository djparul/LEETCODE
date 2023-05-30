# 2574.LeftandRightSumDifferences.py
# https://leetcode.com/problems/left-and-right-sum-differences
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        return [abs(sum(nums[:i+1]) - sum(nums[i:])) for i in range(len(nums))]
        