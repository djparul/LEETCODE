# https://leetcode.com/problems/sort-the-people/
from collections import OrderedDict
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        my_dict = OrderedDict()
        count = len(heights) - 1
        for i,value in enumerate(heights):
            my_dict[value] = names[i]
        names.clear()
        for key in sorted(my_dict.keys(),reverse=True):
            names.append(my_dict[key])
        return names