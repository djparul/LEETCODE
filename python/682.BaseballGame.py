#682.BaseballGame.py
# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        mystack = []
        for i in operations:
            if len(mystack) > 1 and i == '+':
                mystack.append(int(mystack[-1]) + int(mystack[-2]))
            elif mystack and i == 'C':
                mystack.pop()
            elif mystack and i == 'D':
                mystack.append(2*int(mystack[-1]))
            else:
                mystack.append(int(i))
        return sum(mystack)