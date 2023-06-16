# 46.Permutations.py
# https://leetcode.com/problems/permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()
        def backtrack(start, comb, visited):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                comb.append(nums[i])
                visited.add(nums[i])
                backtrack(i+1, comb, visited)
                comb.pop()
                visited.remove(nums[i])
        backtrack(0, [], visited)
        return res