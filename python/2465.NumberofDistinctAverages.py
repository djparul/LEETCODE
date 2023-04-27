# https://leetcode.com/problems/number-of-distinct-averages/
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        myset = set()
        nums.sort()
        for i,v in enumerate(nums):
            j = len(nums) - 1 - i
            if i < j: 
                avg = (nums[i] + nums[j])/2
                j -= 1
                myset.add(avg)
        return len(myset)