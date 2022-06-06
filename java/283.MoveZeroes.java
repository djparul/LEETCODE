# https://leetcode.com/problems/move-zeroes/
class Solution {
    public void moveZeroes(int[] nums) {
        int n = nums.length;
        int i, j=-1;
        for (i = 0; i < n; i++ ) {
            if(nums[i] == 0) {
                int k = 1;
                while(i+k < n && nums[i+k] == 0) {
                    //System.out.println("while");
                    k++;
                }
                if(i+k < n) {
                    nums[i] = nums[i+k];
                    nums[i+k] = 0;
                }
            }    
        }
    }
}