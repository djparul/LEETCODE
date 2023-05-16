# 1598.CrawlerLogFolder.py
# https://leetcode.com/problems/crawler-log-folder/
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        mystack = []
        flag = 0
        for i, val in enumerate(logs):
            if mystack and val == "../":
                mystack.pop()
            elif val == "./":
                pass
            elif val != "../":
                mystack.append(val)
                flag = 1
        print(flag)
        return len(mystack)