# 1331.RankTransformofanArray.py
# https://leetcode.com/problems/rank-transform-of-an-array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res = list()
        mydict = dict()
        x = sorted(set(arr))
        for i in range(len(x)):
            mydict[x[i]] = i+1
        for j in arr:
            res.append(mydict[j])
        return res