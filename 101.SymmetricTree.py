# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common import TreeNode, convertArr, convertTree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2):  # n1:left, n2:right
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)

assert Solution().isSymmetric(convertArr([1,2,2,3,4,4,3])) == True
assert Solution().isSymmetric(convertArr([1,2,2,None,3,None,3])) == False