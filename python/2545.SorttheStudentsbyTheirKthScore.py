# 2545.SorttheStudentsbyTheirKthScore.py
# https://leetcode.com/problems/sort-the-students-by-their-kth-score
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        res = list()
        mymap = dict()
        for i in range(len(score)):
            res.append(score[i][k])
            mymap[score[i][k]] = score[i]
        res.sort(reverse = True)
        for i, val in enumerate(res):
            score[i] = mymap[val]
        return score