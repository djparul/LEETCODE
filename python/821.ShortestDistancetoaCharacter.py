# 821.ShortestDistancetoaCharacter.py
# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        mylist = []
        output = []
        for i, key in enumerate(s):
            if key == c:
                mylist.append(i)
        for i, key in enumerate(s):
            distance = []
            for j in mylist:
                distance.append(abs(i - j))
            output.append(min(distance))
        return output