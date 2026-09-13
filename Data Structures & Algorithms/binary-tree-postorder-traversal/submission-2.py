# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []

        # def postorder(node):
        #     if not node:
        #         return

        #     postorder(node.left)
        #     postorder(node.right)
        #     res.append(node.val)

        # postorder(root)
        # return res

        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                cur = cur.left

        res.reverse()

        return res

