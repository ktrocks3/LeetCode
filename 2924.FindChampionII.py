from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        s = set(i for i in range(n))
        in_edges = set(v for _, v in edges)
        if (len(s) - len(in_edges)) > 1:
            return -1
        s = s.difference(in_edges)
        if len(s) == 1:
            return s.pop()


assert Solution().findChampion(3, [[0, 1], [1, 2]]) == 0, \
    f'Expected:  0, Received: {Solution().findChampion(3, [[0, 1], [1, 2]])}'
assert Solution().findChampion(4, [[0, 2], [1, 3], [1, 2]]) == -1, \
    f'Expected:  -1, Received: {Solution().findChampion(4, [[0, 2], [1, 3], [1, 2]])}'
