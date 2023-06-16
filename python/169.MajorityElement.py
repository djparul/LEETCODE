# 169.MajorityElement.py
# https://leetcode.com/problems/majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        current_majority = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                current_majority = nums[i]
            # count += (1 if current_majority == nums[i] else -1)
            if current_majority == nums[i]:
                count += 1
            else:
                count -= 1
        return current_majority