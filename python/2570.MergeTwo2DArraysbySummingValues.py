# 2570.MergeTwo2DArraysbySummingValues.py
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mydict = dict(nums1)
        for j,val in enumerate(nums2):
            if nums2[j][0] not in mydict:
                mydict[nums2[j][0]] = nums2[j][1]
            else :
                mydict[nums2[j][0]] += nums2[j][1]
        temp = []
        dictList = []  
        for key, value in mydict.items(): 
            temp = [key,value] 
            dictList.append(temp) 
        return sorted(dictList)