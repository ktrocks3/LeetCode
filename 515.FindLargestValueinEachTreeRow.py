# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional, List

from common import TreeNode, convertArr


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        while queue:
            level = []
            m = float('-inf')
            while queue:
                level.append(queue.pop())
            for node in level:
                if not node:
                    continue
                m = max(m, node.val)
                if node.left is not None and node.left.val is not None:
                    queue.append(node.left)
                if node.right is not None and node.right.val is not None:
                    queue.append(node.right)
            if m is not None and m > float('-inf'):
                res.append(m)

        return res


assert Solution().largestValues(convertArr([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9], \
    f'Expected: [1,3,9], Received: {Solution().largestValues(convertArr([1, 3, 2, 5, 3, None, 9]))}'
assert Solution().largestValues(convertArr([1, 2, 3])) == [1, 3], \
    f'Expected: [1,3], Received: {Solution().largestValues(convertArr([1, 2, 3]))}'
assert Solution().largestValues(convertArr([0])) == [0], \
    f'Expected: [0], Received: {Solution().largestValues(convertArr([0]))}'
