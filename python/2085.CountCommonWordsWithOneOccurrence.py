# 2085.CountCommonWordsWithOneOccurrence.py
# https://leetcode.com/problems/count-common-words-with-one-occurrence
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mywords1 = dict()
        mywords2 = dict()
        count = 0
        for elem in words1:
            if elem in mywords1:
                mywords1[elem] += 1
            else:
                mywords1[elem] = 1
        for eleme in words2:
            if eleme in mywords2:
                mywords2[eleme] += 1
            else:
                mywords2[eleme] = 1
        for key in mywords1:
            if key in mywords2 and mywords1[key] == 1 and mywords2[key] == 1:
                count += 1
        return count