# 349.IntersectionofTwoArrays.py
# https://leetcode.com/problems/intersection-of-two-arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myset1 = set(nums1)
        myset2 = set(nums2)
        result = []
        for key in myset1:
            if key in myset2:
                result.append(key)
        return result