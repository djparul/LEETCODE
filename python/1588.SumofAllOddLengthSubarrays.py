# 1588.SumofAllOddLengthSubarrays.py
# https://leetcode.com/problems/sum-of-all-odd-length-subarrays
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(0, len(arr)):
            for j in range(i, len(arr), 2):
                res += sum(arr[i:j+1])
        return res