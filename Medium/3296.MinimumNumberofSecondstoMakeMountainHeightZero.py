from math import sqrt, floor
from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        # Amount of time to reduce by x for worker w is w + 2w + 3w + ... + xw = w ( 1 + 2 + .. + x) = w((x(x+1))/2)
        # So if there was a maximum time T, we could see that the amount of work w could do is equal to
        # T >= w * x(x+1) / 2 so x(x+1) <= 2T/w
        def canFinish(T):
            x = 0
            for w in workerTimes:
                x += floor((-1 + sqrt(1 + 8 * T / w)) / 2)
            return x >= mountainHeight

        low, high = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while low < high:
            mid = (low + high) // 2
            if canFinish(mid):
                high = mid
            else:
                low = mid + 1
        return low


assert Solution().minNumberOfSeconds(4, [2, 1, 1]) == 3, \
  f'Expected: 3, Received: {Solution().minNumberOfSeconds(4, [2, 1, 1])}'
assert Solution().minNumberOfSeconds(10, [3, 2, 2, 4]) == 12, \
  f'Expected: 12, Received: {Solution().minNumberOfSeconds(10, [3, 2, 2, 4])}'
assert Solution().minNumberOfSeconds(5, [1]) == 15, \
  f'Expected: 15, Received: {Solution().minNumberOfSeconds(5, [1])}'
