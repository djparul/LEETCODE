# 2451.OddStringDifference.py
# https://leetcode.com/problems/odd-string-difference
class Solution:
    def oddString(self, words: List[str]) -> str:
        k = len(words[0])
        mydict = list()
        for word in words:
            list1 = list()
            for i in range(len(word) - 1):
                list1.append(ord(word[i+1])-ord(word[i]))
            mydict.append(list1)
        for i in range(len(mydict)):
            if mydict.count(mydict[i]) == 1:
                return words[i]