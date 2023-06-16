# 1408.StringMatchinginanArray.py
# https://leetcode.com/problems/string-matching-in-an-array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            for nword in words:
                if (nword in word) and (not nword == word) and (not nword in res):
                    res.append(nword)
        return res