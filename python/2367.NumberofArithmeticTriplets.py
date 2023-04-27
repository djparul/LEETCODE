# 2367.NumberofArithmeticTriplets.py
# https://leetcode.com/problems/number-of-arithmetic-triplets/ 
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        myset = set()
        count = 0
        for i,v in enumerate(nums):
            myset.add(v)
        for key in myset:
            if key + diff in myset and key + 2*diff in myset:
                count += 1
        return count