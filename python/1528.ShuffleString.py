# 1528.ShuffleString.py
# https://leetcode.com/problems/shuffle-string
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        for i, val in enumerate(s):
            n = indices[i]
            res[n] = val
        return ''.join(res)