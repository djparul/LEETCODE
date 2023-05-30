# 2670.FindtheDistinctDifferenceArray.py
# https://leetcode.com/problems/find-the-distinct-difference-array
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            # print(len(set(nums[:i+1])))
            # print(len(set(nums[i+1:])))
            val = len(set(nums[:i+1])) - len(set(nums[i+1:]))
            result.append(val)
        return result