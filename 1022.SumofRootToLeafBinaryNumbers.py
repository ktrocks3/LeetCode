# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from common import TreeNode, convertArr


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def findPaths(node: TreeNode, path: list) -> list:
            return [] if node is None else [path + [node.val]] if node.left is None else (
                    findPaths(node.left, path + [node.val]) + findPaths(node.right, path + [node.val]))

        paths = findPaths(root, [])
        s = 0
        for path in paths:
            n = 0
            for node in path:
                n = (n * 2) + node
            s += n

        return s


assert Solution().sumRootToLeaf(convertArr([1, 0, 1, 0, 1, 0, 1])) == 22, \
    f'Expected: 22, Received: {Solution().sumRootToLeaf(convertArr([1, 0, 1, 0, 1, 0, 1]))}'
assert Solution().sumRootToLeaf(convertArr([0])) == 0, \
    f'Expected: 0, Received: {Solution().sumRootToLeaf(convertArr([0]))}'
