# 1436.DestinationCity.py
# https://leetcode.com/problems/destination-city/description/
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        myset = set()
        result = ''
        for path,value in enumerate(paths):
            myset.add(paths[path][0])
        for path,value in enumerate(paths):
            if paths[path][1] not in myset:
                result = paths[path][1]
        return result