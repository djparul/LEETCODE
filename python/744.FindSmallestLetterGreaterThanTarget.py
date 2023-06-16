# 744.FindSmallestLetterGreaterThanTarget.py
# https://leetcode.com/problems/find-smallest-letter-greater-than-target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        diff = ord(target) + 26
        char = letters[0]
        for i in letters:
            res = ord(i) - ord(target)
            if res < diff and res > 0:
                diff = res
                char = i
        return char