# 2161.PartitionArrayAccordingtoGivenPivot.py
# https://leetcode.com/problems/partition-array-according-to-given-pivot
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                mid.append(nums[i])
        return left + mid + right
        # return [val for val in nums if val<pivot] + [val for val in nums if val==pivot] + [val for val in nums if val>pivot]