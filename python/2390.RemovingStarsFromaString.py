#2390.RemovingStarsFromaString.py
# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        mystack = []
        for i, val in enumerate(s):
            if mystack and val == '*':
                mystack.pop()
            elif val != '*':
                mystack.append(val)
        return ''.join(mystack)