# 451.SortCharactersByFrequency.py
# https://leetcode.com/problems/sort-characters-by-frequency
class Solution:
    def frequencySort(self, s: str) -> str:
        mydict = dict()
        res = ''
        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        mydict = dict(sorted(mydict.items(), key=lambda x:x[1], reverse = True))
        for key in mydict:
            res += key * mydict[key]
        return res
# Solution 2
# here we sorted in ascending order of values so we need to return res in reverse order that's why we used [::-1]
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         mydict = dict()
#         res = ''
#         for i in s:
#             if i in mydict:
#                 mydict[i] += 1
#             else:
#                 mydict[i] = 1
#         mydict = dict(sorted(mydict.items(), key=lambda x:x[1]))
#         # , reverse = True))
#         for key in mydict:
#             res += key * mydict[key]
#         return res[::-1]