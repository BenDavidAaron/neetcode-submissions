# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        n = root
        r = []
        while q or n:
            while n:
                q.append(n)
                n = n.left
            n = q.pop()
            r.append(n.val)
            n = n.right
        return r