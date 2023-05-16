# 844.BackspaceStringCompare.py
# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def stackInsert(self, s:str, mystack_s:str) -> None:
        for i, val in enumerate(s):
            if mystack_s and val == '#':
                mystack_s.pop()
            elif val != '#':
                mystack_s.append(val)
    def backspaceCompare(self, s: str, t: str) -> bool:
        mystack_s = []
        mystack_t = []
        self.stackInsert(s,mystack_s)
        self.stackInsert(t,mystack_t)
        return mystack_s == mystack_t