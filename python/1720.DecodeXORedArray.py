# 1720.DecodeXORedArray.py
# https://leetcode.com/problems/decode-xored-array
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        for i in range(len(encoded)):
            res = output[-1] ^ encoded[i]
            output.append(res)   
        return output