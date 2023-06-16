# 2586.CounttheNumberofVowelStringsinRange.py
# https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range
class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowel = ['a', 'e', 'i', 'o','u']
        for i, word in enumerate(words):
            if i >= left and i <= right:
                if word[0] in vowel and word[-1] in vowel:
                    count += 1
        return count