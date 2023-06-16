# 153.FindMinimuminRotatedSortedArray.py
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                    left = mid
            else:
                    right = mid
        if nums[right] > nums[left]:
            return nums[0]
        return nums[right]