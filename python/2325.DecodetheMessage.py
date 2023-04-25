# https://leetcode.com/problems/decode-the-message/
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mydict = {' ': ' '}
        whitesp = 0
        ind = 97
        for i in range(len(key)):
            if key[i] not in mydict:
                mydict[key[i]] = chr(ind)
                ind += 1
        result = ''
        for i in range(len(message)):
            result += mydict[message[i]]
        return result