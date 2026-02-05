from typing import List
from collections import deque


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque((t, i) for i, t in enumerate(tickets))
        time = 0

        while True:
            t, i = q.popleft()
            time += 1
            t -= 1

            if t == 0 and i == k:
                return time
            if t > 0:
                q.append((t, i))


assert Solution().timeRequiredToBuy([2, 3, 2], 2) == 6, \
    f'Expected: 6, Received: {Solution().timeRequiredToBuy([2, 3, 2], 2)}'
assert Solution().timeRequiredToBuy([5, 1, 1, 1], 0) == 8, \
    f'Expected: 8, Received: {Solution().timeRequiredToBuy([5, 1, 1, 1], 0)}'
