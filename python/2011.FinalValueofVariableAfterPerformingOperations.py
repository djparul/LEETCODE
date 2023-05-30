# 2011.FinalValueofVariableAfterPerformingOperations.py
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        output = 0
        for i in operations:
            if i == '++X' or i == 'X++':
                output += 1
            else:
                output -= 1
        return output