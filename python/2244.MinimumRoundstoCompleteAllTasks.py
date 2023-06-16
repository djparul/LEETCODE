# 2244.MinimumRoundstoCompleteAllTasks.py
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        res = 0
        mydict = dict()
        for key in tasks:
            if key in mydict: 
                mydict[key] += 1
            else:
                mydict[key] = 1
        for key in mydict:
            while mydict[key]:
                if mydict[key] == 1:
                    return -1
                if mydict[key] % 3 == 0:
                    mydict[key] -= 3
                else:
                    mydict[key] -= 2
                res += 1
        return res