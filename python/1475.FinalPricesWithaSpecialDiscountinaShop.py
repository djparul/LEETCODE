# 1475.FinalPricesWithaSpecialDiscountinaShop.py
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mystack = []
        output = prices
        for i,val in enumerate(prices):
            while mystack and val <= prices[mystack[-1]]:
                output[mystack[-1]] -= val
                mystack.pop()
            mystack.append(i)
        return list(output)