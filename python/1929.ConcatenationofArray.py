# 1929.ConcatenationofArray.py
# https://leetcode.com/problems/concatenation-of-array
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            ans += [nums[i]]
        for i in range(0, len(nums)):
            ans += [nums[i]]
        # for i in range(0, 2 * len(nums)):
        #     ans += [nums[i % (len(nums))]]
        # 
        # return 2*nums
        return ans