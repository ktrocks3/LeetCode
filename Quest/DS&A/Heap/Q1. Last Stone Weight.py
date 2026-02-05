from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, (stone1 - stone2))
        return 0 if not stones else -stones[0]


assert Solution().lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1, \
    f'Expected: 1, Received: {Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])}'
assert Solution().lastStoneWeight([1]) == 1, \
    f'Expected: 1, Received: {Solution().lastStoneWeight([1])}'
