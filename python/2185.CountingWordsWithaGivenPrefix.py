# 2185.CountingWordsWithaGivenPrefix.py
# https://leetcode.com/problems/counting-words-with-a-given-prefix
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        for i in words:
            if i[0:n] == pref:
                count += 1
        return count