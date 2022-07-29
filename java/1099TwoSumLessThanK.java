class Solution {
    public int twoSumLessThanK(int[] nums, int k) {
        int start = 0;
        int end = nums.length -1;
        int sum = 0;
        int res = -1;
        Arrays.sort(nums);
        while(start < end) {
            sum = nums[start] + nums[end];
            if(sum < k){
                res = Math.max(res, sum);
                start++;
            } else {
                end--;
            }
        }
        return res;
    }
}
