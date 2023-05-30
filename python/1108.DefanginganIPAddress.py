# 1108.DefanginganIPAddress.py
# https://leetcode.com/problems/defanging-an-ip-address/
class Solution:
    def defangIPaddr(self, address: str) -> str:
        output = ''
        for i in address:
            if i != '.':
                output += i
            else:
                output += '[.]'
        return output