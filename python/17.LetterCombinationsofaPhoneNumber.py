# 17.LetterCombinationsofaPhoneNumber.py
# https://leetcode.com/problems/letter-combinations-of-a-phone-number 
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mydict = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        res = []
        arr = []
        temp = ''
        def iteratefun(i, temp):
            if i == len(digits):
                if len(temp) > 0:
                    res.append(temp)
                return
            arr = mydict[digits[i]]
            for j, v in enumerate(arr):
                temp += arr[j]
                iteratefun(i + 1, temp)
                temp = temp[:-1]
        iteratefun(0, temp)
        return res