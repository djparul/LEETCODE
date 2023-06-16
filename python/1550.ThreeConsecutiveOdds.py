# 1550.ThreeConsecutiveOdds.py
# https://leetcode.com/problems/three-consecutive-odds
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        flag = False
        for i in arr:
            if i % 2 == 0:
                count = 0
            else:
                count += 1
                if count == 3:
                    flag = True
        return flag