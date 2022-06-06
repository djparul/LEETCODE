# https://leetcode.com/problems/maximum-subarray/
class Solution {
    public int maxSubArray(int[] nums) {
         int n = nums.length;
        //int cur = 0, max_sum = 0;
        int cur = nums[0];
        int max_sum = nums[0]; 
        for (int i=1; i<n; i++) {
            if(cur < 0) {
                cur = nums[i];
            }
            else {
                cur = cur + nums[i];
            }
            max_sum = Math.max(max_sum, cur);
        }
    return max_sum;
    }
}