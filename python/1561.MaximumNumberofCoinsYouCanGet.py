# 1561.MaximumNumberofCoinsYouCanGet.py
# https://leetcode.com/problems/maximum-number-of-coins-you-can-get
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        res = 0
        left = -1
        right = len(piles) - 1
        while left < right:
            left += 2
            res += piles[left]
            right -= 1
        return res