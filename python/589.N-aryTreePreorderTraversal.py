# 589.N-aryTreePreorderTraversal.py
# https://leetcode.com/problems/n-ary-tree-preorder-traversal
# root, left, right
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack, result = [root], []
        while stack:
            cur = stack.pop()
            result.append(cur.val)
            for child in reversed(cur.children):
                stack.append(child) 
        return result