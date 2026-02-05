from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            possible = [(r - 1, c + 1), (r, c + 1), (r + 1, (c + 1))]
            res = []
            for row, col in possible:
                if row >= len(grid) or row < 0 or col < 0 or col >= len(grid[0]) or grid[row][col] <= grid[r][c]:
                    continue
                res.append(dfs(row, col) + 1)
            if len(res) == 0:
                return 0
            cache[(r,c)] = max(res)
            return max(res)

        sol = []
        for i in range(len(grid)):
            sol.append(dfs(i, 0))

        return max(sol)

# print(Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]))
assert Solution().maxMoves([[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]]) == 3
assert Solution().maxMoves([[3, 2, 4], [2, 1, 9], [1, 1, 7]]) == 0
