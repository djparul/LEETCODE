# 884.UncommonWordsfromTwoSentences.py
# https://leetcode.com/problems/uncommon-words-from-two-sentences/
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split()
        s2 = s2.split()
        mydict = dict()
        result = []
        for elements in s1:
            if elements in mydict:
                mydict[elements] += 1
            else:
                mydict[elements] = 1
        for element in s2:
            if element in mydict:
                mydict[element] += 1
            else:
                mydict[element] = 1
        print(mydict)
        for key in mydict:
            if mydict[key] == 1:
                result.append(key)
        return result