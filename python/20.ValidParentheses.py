# 20.ValidParentheses.py
# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        mystack = []
        for i,val in enumerate(s):
            if val == '(' or val == '{' or val == '[':
                mystack.append(val)
            elif mystack and ((val == ')' and mystack[-1] == '(') or (val == '}' and mystack[-1] == '{') or (val == ']' and mystack[-1] == '[')):
                mystack.pop()
            else: 
                return False
        if len(mystack) == 0: # and len(s) % 2 == 0:
            return True
        return False