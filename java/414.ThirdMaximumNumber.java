#https://leetcode.com/problems/third-maximum-number/
class Solution {
    public int thirdMax(int[] nums) {
        Set<Integer> set = new HashSet<Integer>(); 
        PriorityQueue<Integer> pQueue = new PriorityQueue<Integer>(Collections.reverseOrder());
        for(int i = 0; i < nums.length; i++) {
            set.add(nums[i]);
        }
        for(Integer s : set) {
            pQueue.add(s);
        }
        for(int i = 0; i < 3; i++) {
            int M = pQueue.poll();
            if ((i == 0 && set.size() < 3) || i == 2) {
                return M;  
            }
        }
        return 0;
    }
}
