# https://leetcode.com/problems/decode-the-message/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pair_count = 0
        mydict = {}
        for element in nums:
            if element not in mydict:
                mydict[element] = 1
                continue
            mydict[element] += 1
        for key in mydict.keys():
            other_element = key + k
            if other_element in mydict.keys():
                pair_count += mydict[key] * mydict[other_element]
        return pair_count