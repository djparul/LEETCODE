# 1768.MergeStringsAlternately.py
# https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        length = len(word1) + len(word2)
        j = z = 0
        for i in range(length):
            if j < len(word1):
                output += word1[j]
                j += 1
            if z < len(word2):
                i = i + 1
                output += word2[z]
                z += 1
        return output