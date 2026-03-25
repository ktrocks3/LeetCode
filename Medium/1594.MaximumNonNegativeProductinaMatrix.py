from typing import List


class Solution:
    MOD = 10**9 + 7
    def maxProductPath(self, grid: List[List[int]]) -> int:
        dp = [[(0, 0) for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    dp[i][j] = (grid[i][j], grid[i][j])
                    continue
                up = dp[i - 1][j]
                left = dp[i][j - 1]
                if i == 0:
                    up = left
                if j == 0:
                    left = up
                low = min(up[0], left[0])  * grid[i][j]
                high = max(up[1], left[1])  * grid[i][j]
                dp[i][j] = (low, high) if grid[i][j] > 0 else (high, low)
        return dp[-1][-1][1] % self.MOD if dp[-1][-1][1] > -1 else -1


assert Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]]) == -1, \
    f'Expected: -1, Received: {Solution().maxProductPath([[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]])}'
assert Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]]) == 8, \
    f'Expected: 8, Received: {Solution().maxProductPath([[1, -2, 1], [1, -2, 1], [3, -4, 1]])}'
assert Solution().maxProductPath([[1, 3], [0, -4]]) == 0, \
    f'Expected: 0, Received: {Solution().maxProductPath([[1, 3], [0, -4]])}'
