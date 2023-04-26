# https://leetcode.com/problems/first-letter-to-appear-twice/description/
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mydict = {}
        for i , v in enumerate(s):
            if v not in mydict:
                mydict[v] = 1
            else:
                return v