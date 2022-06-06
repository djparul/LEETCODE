# https://leetcode.com/problems/missing-number/
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int Sum = (n*(n+1) )/2;
        for (int i = 0; i < n; i++) {
            Sum = Sum - nums[i];
        }
        return Sum;
    }
}