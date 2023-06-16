# 90.SubsetsII.py
# https://leetcode.com/problems/subsets-ii
# Time complexity -> n*2^n + nlogn ~= n*2^n
# Space complexity -> n*2^n + O(1) ~= n*2^n
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::]) # res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums)  and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res