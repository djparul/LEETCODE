# 1209.RemoveAllAdjacentDuplicatesinStringII.py
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        mystack = []
        for i, val in enumerate(s):
            if mystack and mystack[-1][0] == val:
                mystack[-1][1] += 1
                if mystack[-1][1] == k:
                    mystack.pop()
            else:
                mystack.append([val, 1]) # d,e,1,1
        return ''.join(key*value for key,value in mystack)