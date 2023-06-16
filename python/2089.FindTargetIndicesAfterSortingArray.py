# 2089.FindTargetIndicesAfterSortingArray.py
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = list()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res