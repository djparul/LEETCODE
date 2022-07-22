# https://leetcode.com/problems/flipping-an-image/
class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int temp = -1;
        for(int i = 0; i < image.length; i++) { 
            for(int j = 0; j < image.length/2; j++) {
                temp = image[i][image.length - j -1];
                image[i][image.length -1 - j] = image[i][j];
                image[i][j] = temp;            
            }
        }
        for(int i = 0; i < image.length; i++) {
            for(int j = 0; j < image.length; j++) {
                if(image[i][j] == 0){
                    image[i][j] = 1;
                } else if(image[i][j] == 1){
                    image[i][j] = 0;
                }
            }
        }
        return image;
    }
}
