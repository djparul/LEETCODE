# https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for i,val in enumerate(nums):
            if val in mydict:
                mydict[val] += 1
            else:
                mydict[val] = 1
        for key in mydict:
            if mydict[key] > 1:
                return True
        return False