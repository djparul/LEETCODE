# 2610.ConvertanArrayIntoa2DArrayWithConditions.py
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
from collections import defaultdict
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        mydict = defaultdict(int)
        for i in nums:
            mydict[i] += 1
        output = []
        for i in range(max(mydict.values())):
            res = []
            for key, value in mydict.items():
                if value != 0:
                    mydict[key] -= 1
                    res.append(key)
            output.append(res)            
        return output