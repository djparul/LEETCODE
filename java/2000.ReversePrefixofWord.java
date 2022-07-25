# https://leetcode.com/problems/reverse-prefix-of-word/
class Solution {
    public String reversePrefix(String word, char ch) {
        char[] w = word.toCharArray();
        int end =0 ;
        for(int i = 0; i < word.length(); i++) {
           if(w[i] == ch){
               break;
           }
            else if( i== word.length()-1 && w[word.length()-1] != ch) {
                return word;    
            }
            end = i+1;
        }
        int start = 0;
        
        while(start < end) {
            char temp = w[start];
            w[start] = w[end];
            w[end] = temp;
            start++;
            end--;
        }
        return new String(w);
    }
}
