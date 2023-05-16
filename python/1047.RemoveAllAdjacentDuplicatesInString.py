# 1047. Remove All Adjacent Duplicates In String.py
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        mystack = []
        for i, val in enumerate(s):
            if mystack and mystack[-1] == val:
                mystack.pop()
            else:
                mystack.append(val)
        return ''.join(mystack)