from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        current = intervals[0]
        for i in range(len(intervals)-1):
            if current[1] >= intervals[i+1][0]:
                current[1] = max(current[1], intervals[i+1][1])
            else:
                res.append(current)
                current = intervals[i+1]
        res.append(current)
        return res



assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1,6],[8,10],[15,18]], \
  f'Expected: [[1,6],[8,10],[15,18]], Received: {Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])}'
assert Solution().merge([[1, 4], [4, 5]]) == [[1,5]], \
  f'Expected: [[1,5]], Received: {Solution().merge([[1, 4], [4, 5]])}'
assert Solution().merge([[4, 7], [1, 4]]) == [[1,7]], \
  f'Expected: [[1,7]], Received: {Solution().merge([[4, 7], [1, 4]])}'
assert Solution().merge([[1,4],[2,3]]) == [[1,4]], \
  f'Expected: [[1,7]], Received: {Solution().merge([[1,4],[2,3]])}'
assert Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]) == [[1,10]], \
  f'Expected: [[1,7]], Received: {Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])}'
