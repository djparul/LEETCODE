# 33.SearchinRotatedSortedArray.py
# https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot point
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        pivot = left
        # perform binary search on the appropriate half of the array
        if target >= nums[pivot] and target <= nums[-1]:
            left, right = pivot, len(nums) - 1
        else:
            left, right = 0, pivot - 1
        while left <= right:
            pivot = int((left + right) / 2)
            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        return -1