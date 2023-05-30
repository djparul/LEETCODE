# 2053.KthDistinctStringinanArray.py
# https://leetcode.com/problems/kth-distinct-string-in-an-array/
from collections import OrderedDict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = 0
        output = ''
        mydict = OrderedDict()
        for elements in arr:
            if elements in mydict:
                mydict[elements] += 1
            else:
                mydict[elements] = 1
        for key in mydict:
            if mydict[key] == 1:
                count += 1
                if count == k:
                    output = key
        return output