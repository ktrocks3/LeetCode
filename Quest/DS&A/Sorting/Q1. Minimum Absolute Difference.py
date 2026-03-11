from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minDiff = float("inf")
        arr.sort()
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i] - arr[i-1])

        res = []
        for i in range(1, len(arr)):
            if (arr[i] - arr[i-1]) == minDiff:
                res.append([arr[i-1], arr[i]])

        return res


assert Solution().minimumAbsDifference([4, 2, 1, 3]) == [[1,2],[2,3],[3,4]], \
  f'Expected: [[1,2],[2,3],[3,4]], Received: {Solution().minimumAbsDifference([4, 2, 1, 3])}'
assert Solution().minimumAbsDifference([1, 3, 6, 10, 15]) == [[1,3]], \
  f'Expected: [[1,3]], Received: {Solution().minimumAbsDifference([1, 3, 6, 10, 15])}'
assert Solution().minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14,-10],[19,23],[23,27]], \
  f'Expected: [[-14,-10],[19,23],[23,27]], Received: {Solution().minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27])}'
