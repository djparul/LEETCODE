# 2535.DifferenceBetweenElementSumandDigitSumofanArray.py
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        flag = 0
        res = 0
        for i in nums:
            if i < 10:
                flag = 1
            else:
                flag = 0
                break
        if flag == 1:
            return 0
        else:
            for j in nums:
                if j < 10:
                    res += j
                else:
                    while j > 0:
                        rem = j % 10
                        j = j // 10
                        res += rem
        return abs(res - sum(nums))        