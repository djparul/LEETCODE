# https://leetcode.com/problems/unique-morse-code-words
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lis = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        myset = set()
        for i,val in enumerate(words):
            morse = ''
            for j,value in enumerate(words[i]):
                    pos = ord(value) - ord('a')
                    # get the morse from lis
                    char = lis[pos]
                    # append the morse
                    morse += char
            myset.add(morse)
        return len(myset)