# 14.LongestCommonPrefix.py
# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for i in range(1, len(strs)):
            cur_common = ''
            for j in range(0, len(strs[i])):
                if len(strs[i]) > j and len(result) > j and strs[i][j] == result[j]:
                    cur_common += strs[i][j]
                else:
                    break
            result = cur_common
        return result