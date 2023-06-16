# 506.RelativeRanks.py
# https://leetcode.com/problems/relative-ranks
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = list()
        for i, sc in enumerate(score):
            heappush(pq,(-sc,i))

        res = [0] * len(score)
        place = 1

        while pq:
            rank_sc = heappop(pq)[1]
            if place > 3:
                rank = str(place) 
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"

            res[rank_sc] = rank
            place += 1

        return res