# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy = nums.copy()
        copy.sort()
        myset = {}
        for x, val in enumerate(copy):
            if copy[x] not in myset.keys():
                myset[val] = x
        for i, val in enumerate(nums):
            nums[i] = myset[val]
        return nums
# nums
# sort -> n
# lookup
