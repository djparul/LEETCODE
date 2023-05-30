# 2215.FindtheDifferenceofTwoArrays.py
# https://leetcode.com/problems/find-the-difference-of-two-arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[],[]]
        myset1 = set(nums1)
        myset2 = set(nums2)
        answer[0] = (list(myset1-myset2))
        answer[1] = (list(myset2-myset1))
        return answer