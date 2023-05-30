# 1534.CountGoodTriplets.py
# https://leetcode.com/problems/count-good-triplets
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        for i in range(0, len(arr) - 2):
            for j in range(i+1, len(arr) - 1):
                # if :
                    for k in range(j+1, len(arr)):
                        if (abs(arr[i] - arr[j])) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                            res += 1
        return res