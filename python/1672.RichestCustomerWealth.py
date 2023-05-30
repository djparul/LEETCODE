# 1672.RichestCustomerWealth.py
# https://leetcode.com/problems/richest-customer-wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            amount = 0
            for j in range(len(accounts[i])):
                amount += accounts[i][j]
                if amount > richest:
                    richest = amount
        return richest