# 39.CombinationSum.py
# https://leetcode.com/problems/combination-sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, cur, total):
            if total > target or i >= len(candidates):
                return
            if target == total:
                res.append(cur.copy())
                return
            
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)
        backtrack(0, [], 0)
        return res