from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, ans, d = 0, 0, 0, 0

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(command):
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in obstacle_set:
                        break
                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)
        return ans


assert Solution().robotSim([4, -1, 3], []) == 25, \
    f'Expected: 25, Received: {Solution().robotSim([4, -1, 3], [])}'
assert Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65, \
    f'Expected: 65, Received: {Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]])}'
assert Solution().robotSim([6, -1, -1, 6], [[0, 0]]) == 36, \
    f'Expected: 36, Received: {Solution().robotSim([6, -1, -1, 6], [[0, 0]])}'
