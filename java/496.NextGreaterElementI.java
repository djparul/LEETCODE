#https://leetcode.com/problems/next-greater-element-i/
class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int n1 = nums1.length;
        int[] ans = new int[n1];
        for(int i = 0; i < n1; i++) {
            for(int j = 0; j < nums2.length; j++) {
                if(nums1[i] == nums2[j] && j != nums2.length-1){
                    for(int z = j+1; z < nums2.length; z++) {
                        if(nums2[z] > nums2[j]) {
                            ans[i] = nums2[z];
                            break;  
                        } else {
                            ans[i] = -1;
                        }
                    }  
                } if(nums1[i] == nums2[j] && j == nums2.length-1){
                    ans[i] = -1;
                }    
            }
        }
        return ans;
    }
}