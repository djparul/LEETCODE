#https://leetcode.com/problems/palindrome-number/
class Solution {
    public boolean isPalindrome(int x) {
        int num = x;
        int rev = 0, rem = 0;
        while( x > 0 ) {
            rem = x % 10;   
            rev = rev*10 + rem;
            x = x / 10;
            //System.out.println("Rev = " + rev + " Rem = " + rem + " x = " + x);
        }
        if( rev == num ) {
            return true;
        }
        return false;
    }
}