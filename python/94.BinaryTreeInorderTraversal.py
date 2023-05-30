# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# -----------------
# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# SOLUTION 1: Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        result = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right     
        return result
# -----------------
# SOLUTION 2: Recurrsive
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         result = []
#         def inorder(root):
#             if not root:
#                 return 
#             inorder(root.left)
#             result.append(root.val)
#             inorder(root.right)
#         inorder(root)
#         return result