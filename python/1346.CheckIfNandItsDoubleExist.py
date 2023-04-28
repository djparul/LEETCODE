# 1346.CheckIfNandItsDoubleExist.py
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mydict = dict()
        for i,val in enumerate(arr):
            if val in mydict:
                mydict[val] += 1
            else:
                mydict[val] = 1
        for i in mydict:   
            if (i == 0 and mydict[0]> 1) or (i and 2*i in mydict):
                return True 
        return False