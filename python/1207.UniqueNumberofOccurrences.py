# 1207.UniqueNumberofOccurrences.py
# https://leetcode.com/problems/unique-number-of-occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mydict = dict()
        myset = set()
        for key in arr:
            mydict[key] = arr.count(key)
        for key, value in mydict.items():
            myset.add(value) 
        return (sum(myset) == len(arr))