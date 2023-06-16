# 739.DailyTemperatures.py
# https://leetcode.com/problems/daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mystack = []
        res = [0]* len(temperatures)
        for i in range(len(temperatures)):
            while mystack and temperatures[mystack[-1]] < temperatures[i]:
                    j = mystack.pop()
                    res[j] = i - j
            mystack.append(i)    
        return res