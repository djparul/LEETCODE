#https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
class Solution {
    public int maxProduct(int[] nums) {
    PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
    for(int i = 0; i < nums.length; i++) {
        pQueue.add(nums[i]);
    }
    return (pQueue.poll()-1)*(pQueue.poll()-1);
    }
}