# https://leetcode.com/problems/first-unique-character-in-a-string/description/
import sys
class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = sys.maxsize
        mydict = {}
        for i,key in enumerate(s):
            if key in mydict:
                mydict[key].append(i)
            else:
                mydict[key] = [i]
        for key, value in mydict.items():
            if len(value) == 1 and value[0] < result:
                    result = value[0]
        if result == sys.maxsize:
            print(result)
            result = -1
        return result