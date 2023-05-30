# 2433.FindTheOriginalArrayofPrefixXor.py
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = 0
        for i in range(1, len(pref)):
            res ^= pref[i - 1]
            pref[i] = res ^ pref[i]
        return pref