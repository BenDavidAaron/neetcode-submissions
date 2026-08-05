# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = []
        r = []
        n = root
        while n or q:
            if n:
                r.append(n.val)
                q.append(n.right)
                n = n.left
            else:
                n = q.pop()
        return r
