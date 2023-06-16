# 2706.BuyTwoChocolates.py
# https://leetcode.com/problems/buy-two-chocolates
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum_two = prices[0] + prices[1]
        if money >= sum_two:
            return money - sum_two
        else:
            return money
