# 2206.DivideArrayIntoEqualPairs.py
# https://leetcode.com/problems/divide-array-into-equal-pairs/description/
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # nums.sort()
        print(nums)
        mydict = {}
        for i,v in enumerate(nums):
            if v not in mydict:
                mydict[v] = 1
            else:
                mydict[v] += 1
        for val in mydict:
            if mydict[val] % 2 == 1:
                return False
        return True