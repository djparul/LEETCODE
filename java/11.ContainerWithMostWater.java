# https://leetcode.com/problems/container-with-most-water/
class Solution {
    public int maxArea(int[] height) {
    int max = 0;
    int area = 0;
    for(int i = 0; i < height.length; i++){
        for(int j = i+1; j < height.length; j++){
            area = Math.max(area, Math.min(height[j], height[i]) * (j - i));
            // System.out.println(" i = " + i + " j = " + j + " area = " + area) ;
        }
    }
    return area;
    }
}