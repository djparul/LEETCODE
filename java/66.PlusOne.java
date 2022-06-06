#https://leetcode.com/problems/plus-one/
class Solution {
    public int[] plusOne(int[] digits) {
        // Case 1 All are 9                
        int arr[];
        boolean flag=true; 
         for(int i=0;i<digits.length;i++) {
             if(digits[i]!=9) {
                 flag=false;
                 break;
             }
         }
         if(flag == true) {
             arr=new int[digits.length+1];
             Arrays.fill(arr,0);
             arr[0]=1;
             return arr;
         } else {  // Case 2 Last digit is 9
                if(digits[digits.length-1] == 9) {
                int carry = 1;   
                int i = digits.length-1;
                while(i >= 0) {
                    int sum = carry+digits[i];
                    digits[i] = sum % 10;
                    carry = sum / 10;
                    if(carry == 0) {
                        break;
                    }
                    i--;
                }
               } else {             //Case 3: Last Digit not 9
                   digits[digits.length-1]++;
               }
         }
         return digits;
    }
}