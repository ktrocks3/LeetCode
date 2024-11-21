from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [['E'] * n for _ in range(m)]  # 'E' for empty, 'G' for guard, 'W' for wall

        # Mark guards and walls on the grid
        for x, y in guards:
            grid[x][y] = 'G'
        for x, y in walls:
            grid[x][y] = 'W'

        # Mark cells guarded by each guard
        def mark_guarded(x, y, dx, dy):
            while 0 <= x < m and 0 <= y < n:
                if grid[x][y] in {'G', 'W'}:
                    break
                grid[x][y] = 'V'  # Mark as guarded
                x += dx
                y += dy

        # Simulate guard line-of-sight
        for x, y in guards:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                mark_guarded(x + dx, y + dy, dx, dy)

        # Count unguarded cells
        unguarded_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'E':
                    unguarded_count += 1

        return unguarded_count


assert Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]) == 7, \
    f"Expected: 7, Actual: {Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]])}"

assert Solution().countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]]) == 4, \
    f"Expected: 4, Actual: {Solution().countUnguarded(3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]])}"
