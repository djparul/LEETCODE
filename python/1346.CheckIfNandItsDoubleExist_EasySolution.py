# 1346.CheckIfNandItsDoubleExist_EasySolution.py
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        myset = set(arr) - {0}
        for i in myset:
            if 2*i in myset:
                return True 
        return False