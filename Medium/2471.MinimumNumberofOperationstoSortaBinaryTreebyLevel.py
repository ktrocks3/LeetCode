from collections import deque
from typing import Optional
from common import *


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = 0
        while q:
            a = []
            for _ in range(len(q)):
                node = q.popleft()
                a.append(node.val)
                if node.left and node.left.val:
                    q.append(node.left)
                if node.right and node.right.val:
                    q.append(node.right)
            n = len(a)
            a = sorted(range(n), key=lambda i: a[i])

            vis = [False] * n
            ans += n
            for v in a:
                if vis[v]:
                    continue
                while not vis[v]:
                    vis[v] = True
                    v = a[v]
                ans -= 1
        return ans


assert Solution().minimumOperations(convertArr([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10])) == 3, \
    f'Expected: 3, Received: {Solution().minimumOperations(convertArr([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10]))}'
assert Solution().minimumOperations(convertArr([1, 3, 2, 7, 6, 5, 4])) == 3, \
    f'Expected: 3, Received: {Solution().minimumOperations(convertArr([1, 3, 2, 7, 6, 5, 4]))}'
assert Solution().minimumOperations(convertArr([1, 2, 3, 4, 5, 6])) == 0, \
    f'Expected: 0, Received: {Solution().minimumOperations(convertArr([1, 2, 3, 4, 5, 6]))}'
