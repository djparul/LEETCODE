# 946.ValidateStackSequences.py
# https://leetcode.com/problems/validate-stack-sequences
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        mystack = []
        j = 0
        for i in range(len(pushed)):
            mystack.append(pushed[i])
            while j < len(popped) and len(mystack) > 0 and mystack[-1] == popped[j]:
                mystack.pop()
                j += 1
        return len(mystack) == 0