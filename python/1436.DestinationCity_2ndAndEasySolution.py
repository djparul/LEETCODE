# 1436.DestinationCity.py
# https://leetcode.com/problems/destination-city/description/
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mysource = set()
        mydestination = set()
        for path,value in enumerate(paths):
            mysource.add(paths[path][0])
            mydestination.add(paths[path][1])
        return list(mydestination - mysource)[0]