# https://leetcode.com/problems/two-out-of-three/
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = dict()
        for i,v in enumerate(nums1):
            if v not in result:
                result[v] = [1,0,0]
        for i,v in enumerate(nums2):
            if v not in result:
                result[v] = [0,1,0]
            else:
                result[v][1] = 1
        for i,v in enumerate(nums3):
            if v not in result:
                result[v] = [0,0,1]
            else:
                result[v][2] = 1
        result_key = []
        for key in result:
            count = 0
            for value in result[key]:
                count += value
            if count > 1:
                result_key.append(key)
        return result_key