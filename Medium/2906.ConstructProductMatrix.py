from typing import List


class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        prefix, suffix = [1], [1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                prefix.append(prefix[-1] * grid[i][j] % 12345)
                suffix.append(suffix[-1] * grid[len(grid) - i - 1][len(grid[0]) - j - 1] % 12345)
        suffix.reverse()
        p = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(p)):
            for j in range(len(p[0])):
                p[i][j] = prefix[i * len(p[0]) + j] * suffix[i * len(p[0]) + j + 1] % 12345
        return p


assert Solution().constructProductMatrix([[1, 2], [3, 4]]) == [[24, 12], [8, 6]], \
    f'Expected: [[24,12],[8,6]], Received: {Solution().constructProductMatrix([[1, 2], [3, 4]])}'
assert Solution().constructProductMatrix([[12345], [2], [1]]) == [[2], [0], [0]], \
    f'Expected: [[2],[0],[0]], Received: {Solution().constructProductMatrix([[12345], [2], [1]])}'
