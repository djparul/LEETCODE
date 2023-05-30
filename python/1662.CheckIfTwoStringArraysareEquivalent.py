# 1662.CheckIfTwoStringArraysareEquivalent.py
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
# Solution 1:
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1, string2 = str(), str()
        for i in word1:
            string1 += i
        for j in word2:
            string2 += j
        return string1 == string2
# Solution 2:
        # return ''.join(word1) == ''.join(word2)