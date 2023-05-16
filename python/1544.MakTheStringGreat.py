# 1544.MakTheStringGreat.py
# https://leetcode.com/problems/make-the-string-great
class Solution:
    def makeGood(self, s: str) -> str:
        mystack = []
        for i in range(len(s)):
            if mystack and mystack[-1] == s[i].swapcase():
                mystack.pop()
            else:
                mystack.append(s[i])
        return ''.join(mystack)