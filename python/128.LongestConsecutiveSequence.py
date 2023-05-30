# 128.LongestConsecutiveSequence.py
# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_count = 0
        if len(nums) == 1 or (len(nums) == 2 and nums[0] == nums[1]) :
            return 1
        if (len(nums) == 2 and nums[0] + 1 == nums[1]) :
            return 2
        for i in range(0, len(nums) - 1):
            if (nums[i] + 1 == nums[i+1]):
                count += 1
            elif (nums[i] == nums[i+1]):
                continue
            else:
                count = 1
            if count > max_count:
                max_count = count
        return max_count