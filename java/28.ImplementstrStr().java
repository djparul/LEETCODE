#https://leetcode.com/problems/implement-strstr/
class Solution {
    // 856ms, faster than 32.79% of Java online submissions 
    // 117.5 MB, less than 23.31% of Java online submissions
    
    
    public int strStr(String haystack, String needle) {
        if(needle.length() == 0) {
            return 0;
        }
        
        if(haystack.length() == 0){ //implies needle is not empty
            return -1;
        }
        
        int nLen = needle.length();
        for(int i = 0; i < haystack.length() - (nLen-1); i++){
            //System.out.println(haystack.substring(i, i + nLen));
            if(haystack.substring(i, i+ nLen).equals(needle)){
                return i;
            }
        }
        
        return -1;
    }
}
    