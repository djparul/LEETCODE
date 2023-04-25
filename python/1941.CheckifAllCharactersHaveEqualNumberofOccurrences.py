# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        mydict = {}
        for i,val in enumerate(s):
            if val in mydict:
                mydict[val] += 1
            else:
                mydict[val] = 1
        prev = -1
        for value in mydict.values():
            if prev != -1:
                if prev != value:
                    return False
            prev = value
        return True     