# 2341. Maximum Number of Pairs in Array
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        mydict = dict()
        count = pair = 0
        for i,v in enumerate(nums):
            if v not in mydict:
                mydict[v] = 1
            else:
                mydict[v] += 1
        for val in mydict:
            if mydict[val] % 2 == 0:
                pair += int(mydict[val] / 2)
            else:
                count += 1           
                pair += int(mydict[val] / 2)
        return [pair, count]