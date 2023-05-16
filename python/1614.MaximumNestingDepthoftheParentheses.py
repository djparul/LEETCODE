# 1614.MaximumNestingDepthoftheParentheses.py
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        mystack = []
        for i,val in enumerate(s):
            if val == '(':
                mystack.append(val)
                count = max(count, len(mystack))
            elif val == ')':
                mystack.pop()
        return count