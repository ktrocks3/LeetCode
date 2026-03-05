from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current_alt = 0
        for g in gain:
            current_alt += g
            if current_alt > highest:
                highest = current_alt

        return highest

assert Solution().largestAltitude([-5, 1, 5, 0, -7]) == 1, \
  f'Expected: 1, Received: {Solution().largestAltitude([-5, 1, 5, 0, -7])}'
assert Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2]) == 0, \
  f'Expected: 0, Received: {Solution().largestAltitude([-4, -3, -2, -1, 4, 3, 2])}'
