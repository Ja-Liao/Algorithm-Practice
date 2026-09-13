# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, value):
            nonlocal res
            if not node:
                return 0

            if node.val >= value:
                res += 1

            if node.left:
                dfs(node.left, max(value, node.val))
            if node.right:
                dfs(node.right, max(value, node.val))

        dfs(root, -float('inf'))

        return res