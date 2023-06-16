# 154.FindMinimuminRotatedSortedArrayII.py
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                if nums[mid] == nums[left]:
                    left += 1
                elif nums[left] < nums[mid]:
                    right = mid - 1
                else:
                    right = mid 
            elif nums[right] < nums[mid]:
                    left = mid + 1
            else:
                    right = mid
        return nums[left]