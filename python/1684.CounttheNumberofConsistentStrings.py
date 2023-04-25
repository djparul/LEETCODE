# https://leetcode.com/problems/count-the-number-of-consistent-strings/
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        myset = set()
        for element in allowed:
            myset.add(element)
        count = 0
        for i in range(len(words)):
            for j,k in enumerate(words[i]):
                if k not in myset:
                    break
                else:
                    if j == len(words[i]) - 1:
                        count += 1
        return count