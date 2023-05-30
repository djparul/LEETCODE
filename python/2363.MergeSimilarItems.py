# 2363.MergeSimilarItems.py
# https://leetcode.com/problems/merge-similar-items
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        mydict = dict()
        for i in range(len(items1)):
            if items1[i][0] not in mydict:
                mydict[items1[i][0]] = items1[i][1]
        for j in range(len(items2)):
            if items2[j][0] not in mydict:
                mydict[items2[j][0]] = items2[j][1]
            elif items2[j][0] in mydict:
                mydict[items2[j][0]] += items2[j][1]
        return sorted(mydict.items())