# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False
        arr = [0 for x in range(26)]
        for i in range(len(sentence)):
            arr[ord(sentence[i]) - ord('a')] = 1
        product = 1
        for i,j in enumerate(arr):
            product *= arr[i]
        return (product > 0)