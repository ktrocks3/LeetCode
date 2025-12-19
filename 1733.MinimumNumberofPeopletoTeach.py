from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        pass


assert Solution().minimumTeachings(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]]) == 1, \
  f'Expected: 1, Received: {Solution().minimumTeachings(2, [[1], [2], [1, 2]], [[1, 2], [1, 3], [2, 3]])}'
assert Solution().minimumTeachings(3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]]) == 2, \
  f'Expected: 2, Received: {Solution().miniqmumTeachings(3, [[2], [1, 3], [1, 2], [3]], [[1, 4], [1, 2], [3, 4], [2, 3]])}'