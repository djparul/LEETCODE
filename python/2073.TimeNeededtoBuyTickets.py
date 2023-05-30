# 2073.TimeNeededtoBuyTickets.py
# https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        check = tickets[k] # 2
        for i,v in enumerate(tickets):
            if v >= check:
                if k >= i: 
                    result += check # result =2+2+2
                else:
                    result += check-1
            else:
                result += v
        return result