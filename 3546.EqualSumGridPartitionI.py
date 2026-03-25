from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]

        total = sum(row_sums)

        # Check horizontal cut
        curr = 0
        for i in range(m - 1):   # cut after row i, so both parts non-empty
            curr += row_sums[i]
            if curr * 2 == total:
                return True

        # Check vertical cut
        curr = 0
        for j in range(n - 1):   # cut after col j, so both parts non-empty
            curr += col_sums[j]
            if curr * 2 == total:
                return True

        return False


assert Solution().canPartitionGrid([[1, 4], [2, 3]]) == True, \
    f'Expected: True, Received: {Solution().canPartitionGrid([[1, 4], [2, 3]])}'
assert Solution().canPartitionGrid([[1, 3], [2, 4]]) == False, \
    f'Expected: False, Received: {Solution().canPartitionGrid([[1, 3], [2, 4]])}'
assert Solution().canPartitionGrid([[28443],[33959]]) == False, \
    f'Expected: False, Received: {Solution().canPartitionGrid([[28443],[33959]])}'
