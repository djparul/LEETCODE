# 71.SimplifyPath.py
# https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        mystack = []
        path_split = path.split('/')
        print(path_split)
        for i,val in enumerate(path_split):
            if mystack and val == '..':
                mystack.pop()
            elif val not in ['.', '', '..']:
                mystack.append(val)
        return '/' + '/'.join(mystack)