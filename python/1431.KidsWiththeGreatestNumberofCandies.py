# 1431.KidsWiththeGreatestNumberofCandies.py
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = candies[0]
        output = list()
        for i in range(len(candies)):
            if candies[i] > greatest:
                greatest = candies[i]
        # we have the value of no of greatest candy
        for j in range(0,len(candies)):
            if candies[j] == greatest or candies[j] + extraCandies >= greatest:
                output.append(True)
            else: 
                output.append(False)
        return output
        