# https://leetcode.com/problems/two-out-of-three/
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        myset1 = set(nums1)
        myset2 = set(nums2)
        myset3 = set(nums3)
        mydict = dict()
        for key in myset1:
            mydict[key] = 1
        for key in myset2:
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] += 1
        for key in myset3:
            if key not in mydict:
                mydict[key] = 1
            else:
                mydict[key] += 1
        result = []
        for k in mydict:
            if mydict[k] > 1:
                result.append(k)
        return result