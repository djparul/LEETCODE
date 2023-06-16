# 1491.AverageSalaryExcludingtheMinimumandMaximumSalary.py
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary
class Solution:
    def average(self, salary: List[int]) -> float:
        return ((sum(salary) - min(salary) - max(salary))/(len(salary) - 2))
        # salary.sort()
        # return (sum(salary[1:len(salary) - 1]) / (len(salary) - 2))