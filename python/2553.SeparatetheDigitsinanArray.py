#  2553.SeparatetheDigitsinanArray.py
# https://leetcode.com/problems/separate-the-digits-in-an-array
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ''
        output = list()
        for i in nums:
            s += str(i)
        for i in range(len(s)):
            output.append(int(s[i]))
        return output