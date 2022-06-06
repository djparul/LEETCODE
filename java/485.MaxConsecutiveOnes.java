#https://leetcode.com/problems/max-consecutive-ones/
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int count = 1;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0){
                count++;
            } else {
                if(max < count){
                    max = count;
                }
                count = 1;
            }
        }
        if(max < count){
                    max = count;
                }
        max = max-1;
        return max;
    }
}
