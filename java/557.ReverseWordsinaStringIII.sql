# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution {
    public String reverseWords(String s) {
        char[] ch = s.toCharArray();
        int len = s.length();
        if(len == 1) {
            return s;   
        }
        int l = 0, r = 0;
        while( l < len){
            while(r < len && ch[r] != ' '){
                r++;
            } 
            if(r == len-1 && ch[r] != ' '){
                char z = ch[r];
                ch[r] = ch[l];
                ch[l] = z;
            }
            int nl = l, nr = r-1;
            while(nl < nr && nl < len && nr < len && nr > 0){
                char temp = ch[nl];
                ch[nl] = ch[nr];
                ch[nr] = temp ;
                nl++;
                nr--;
            }
            l = r+1;
            r = l;
        }
        return new String(ch);
    }
}
