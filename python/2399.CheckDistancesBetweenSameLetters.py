# 2399.CheckDistancesBetweenSameLetters.py
# https://leetcode.com/problems/check-distances-between-same-letters
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        mydict = dict()
        for i,key in enumerate(s):
            if key in mydict:
                mydict[key] = i - mydict[key] - 1
            else:
                mydict[key] = i
        for key in mydict:
            if mydict[key] == distance[ord(key) - ord('a')]:
                continue
            else: 
                return False
        return True