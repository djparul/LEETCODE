# 1773.CountItemsMatchingaRule.py
# https://leetcode.com/problems/count-items-matching-a-rule
# Solution 1:
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        rule = {'type' : 0, 'color' : 1, 'name' : 2}
        for i in range(len(items)):
            x = rule[ruleKey]
            if items[i][x] == ruleValue:
                count += 1
        return count
# Solution 2:
# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         count = 0
#         for i in range(len(items)):
#             if ruleKey == 'type' and items[i][0] == ruleValue:
#                 count += 1

#             elif ruleKey == 'color' and items[i][1] == ruleValue:
#                 count += 1

#             elif ruleKey == 'name' and items[i][2] == ruleValue:
#                 count += 1
#         return count