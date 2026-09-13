# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        cur = root
        stack = []

        while cur or stack:
            if cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        
        return res