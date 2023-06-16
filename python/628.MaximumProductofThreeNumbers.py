# 628.MaximumProductofThreeNumbers.py
# https://leetcode.com/problems/maximum-product-of-three-numbers
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        positive = heapq.nlargest(3,nums)
        negative = heapq.nsmallest(2,nums)
        return max(positive[0]*positive[1]*positive[2], negative[0]*negative[1]*positive[0])
# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])