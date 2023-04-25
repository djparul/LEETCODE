# https://leetcode.com/problems/sum-of-unique-elements/description/
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mydict = {}
        sum = 0
        for i,v in enumerate(nums):
            if v in mydict:
                mydict[v] += 1
            else:
                mydict[v] = 1
        for key in mydict.keys():
            if mydict[key] == 1:
                sum += key
        return sum