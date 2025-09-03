from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (-p[1], p[0]))
        count = 0
        for i in range(len(points)):
            minimum = float('inf')
            for j in range(i+1, len(points)):
                if points[i][0] <= points[j][0] < minimum:
                    minimum = points[j][0]
                    count += 1
        return count




assert Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]]) == 0, \
  f'Expected: 0, Received: {Solution().numberOfPairs([[1, 1], [2, 2], [3, 3]])}'
assert Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]]) == 2, \
  f'Expected: 2, Received: {Solution().numberOfPairs([[6, 2], [4, 4], [2, 6]])}'
assert Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]]) == 2, \
  f'Expected: 2, Received: {Solution().numberOfPairs([[3, 1], [1, 3], [1, 1]])}'
assert Solution().numberOfPairs([[0,3],[2,4],[0,6]]) == 2, \
  f'Expected: 2, Received: {Solution().numberOfPairs([[0,3],[2,4],[0,6]])}'
assert Solution().numberOfPairs([[0,4],[5,2],[4,1],[6,2]]) == 3, \
  f'Expected: 3, Received: {Solution().numberOfPairs([[0,4],[5,2],[4,1],[6,2]])}'