# 1572.MatrixDiagonalSum.py
# https://leetcode.com/problems/matrix-diagonal-sum
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        for i in range(len(mat)):
            res += mat[i][i] + mat[i][len(mat)-1-i]
        if len(mat) % 2 == 0:
            return res
        index = int(len(mat)/2)
        return res - mat[index][index]