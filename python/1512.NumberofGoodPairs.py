# https://leetcode.com/problems/number-of-good-pairs/
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mydict = {}
        result = 0
        for n in nums:
            if n in mydict.keys():
                mydict[n] += 1
            else:
                mydict.update({n : 1})
        for key in mydict.keys():
            val = mydict[key]
            if val > 1:
                result += val*(val-1)/2

        return int(result)