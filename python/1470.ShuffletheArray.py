# 1470.ShuffletheArray.py
# https://leetcode.com/problems/shuffle-the-array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output += [nums[i]]
            output += [nums[i+n]]
        return output