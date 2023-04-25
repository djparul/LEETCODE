# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 1 or x == 2):
            return 1
        for n in range(1,int(x+1/2)):
            if(n*n == x):
                return int(n)
            elif(n*n > x):
                return int(n-1)
            
        return 0