# 1636.SortArraybyIncreasingFrequency.py
# https://leetcode.com/problems/sort-array-by-increasing-frequency
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mydict = {}
        myfreq = {}
        result = []
        for i, v in enumerate(nums):
            if v not in mydict:
                mydict[v] = 1
            else:
                mydict[v] += 1
        for val in mydict:
            if mydict[val] not in myfreq:
                myfreq[mydict[val]] = [val]
            else:
                myfreq[mydict[val]].append(val)
        myfreq = dict(sorted(myfreq.items()))
        for value in myfreq:
            arr = sorted(myfreq[value],reverse=True)
            for k in arr:
                for j in range(0,value):
                    result.append(k)
        return result