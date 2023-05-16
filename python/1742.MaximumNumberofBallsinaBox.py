# 1742.MaximumNumberofBallsinaBox.py
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = highLimit - lowLimit + 1
        mydict = dict()
        for key in range(1,highLimit+1):
                mydict[key] = 0 
        for i in range(lowLimit, highLimit+1):
            sum = 0
            while i > 0:
                rem = i % 10  #1,2,3
                i = i // 10   #32,3,0
                sum += rem #1,3,6
            mydict[sum] += 1
        mydict = sorted(mydict.items(), key=lambda x:x[1], reverse = True)
        print(mydict)
        x = list(mydict)[0][1]
        return x