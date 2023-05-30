# 383.RansomNote.py
# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myransom = dict()
        mymagazine = dict()
        for i, v in enumerate(ransomNote):
            if v in myransom:
                myransom[v] += 1
            else:
                myransom[v] = 1
        for j, v in enumerate(magazine):
            if v in mymagazine:
                mymagazine[v] += 1
            else:
                mymagazine[v] = 1
        for key in myransom:
            if key in mymagazine and myransom[key] <= mymagazine[key]:
                pass
            else:
                return False
        return True