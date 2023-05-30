# 2678.NumberofSeniorCitizens.py
# https://leetcode.com/problems/number-of-senior-citizens
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            s = details[i]
            if int(s[11:13]) > 60:
                count += 1
        return count