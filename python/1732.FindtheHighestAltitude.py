# 1732.FindtheHighestAltitude.py
# https://leetcode.com/problems/find-the-highest-altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_no = 0
        for i in range(1,len(gain)):
            gain[i] += gain[i-1]
        if max_no > max(gain):
            return 0
        return max(gain)