#https://leetcode.com/problems/remove-element/
class Solution {
    public int removeElement(int[] nums, int val) {
        int n = nums.length; 
        int i, j = -1;
        for ( i = 0; i < n; i++) {
            if (nums[i] == val) {
                int k = 1;
                while (i+k < n && nums[i+k] == val) {
                    k++;
                }
                if (i+k < n) {
                    nums[i] = nums[i+k];
                    nums[i+k] = val;
                    j = i;
                }
            } 
        }
        for ( i = 0; i < n; i++) {
            if (nums[i] == val) {
                return i;
            }
        }
    return n;    
    }
}