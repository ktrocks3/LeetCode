from typing import List
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(-(((l + 1) / (r + 1)) - (l / r)), l, r) for l, r in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            _, l, r = heapq.heappop(heap)
            l, r = l + 1, r + 1
            heapq.heappush(heap, (-(((l + 1) / (r + 1)) - (l / r)), l, r))
        return round(sum((l/r) for _,l,r in heap)/len(heap),5)


assert Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2) == 0.78333, \
    f'Expected: 0.78333, Received: {Solution().maxAverageRatio([[1, 2], [3, 5], [2, 2]], 2)}'
assert Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4) == 0.53485, \
    f'Expected: 0.53485, Received: {Solution().maxAverageRatio([[2, 4], [3, 9], [4, 5], [2, 10]], 4)}'
