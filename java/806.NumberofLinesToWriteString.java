#https://leetcode.com/problems/number-of-lines-to-write-string/
class Solution {
    public int[] numberOfLines(int[] widths, String s) {
        int[] result = new int[2];
        int lines = 1, width_last_line = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            int ascii = ch;
            int j = ascii % 97;
            // lines = 
            
            width_last_line = width_last_line + widths[j];
            if (width_last_line > 100) {
                width_last_line = widths[j];
                lines ++;
            }
        }
        result[0] = lines;
        result[1] = width_last_line;
        
        return result;
    }
}