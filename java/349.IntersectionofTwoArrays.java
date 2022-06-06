#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Set<Integer> setnums1 = new HashSet<>();
        Set<Integer> setnums2 = new HashSet<>();
        int i = 0;
        for(int n : nums1) {
            setnums1.add(n);
        }
        for(int n : nums2) {
            if(setnums1.contains(n)){
                setnums2.add(n);    
            }
        }
        int[] ans = new int[setnums2.size()];
        for(int n : setnums2) {
            ans[i++] = n;
        }
        return ans;
    }
}