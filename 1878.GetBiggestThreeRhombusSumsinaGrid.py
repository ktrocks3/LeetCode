from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        biggest = [-1, -1, -1]

        def compareBiggest(x: int):
            if x == biggest[0] or x == biggest[1] or x == biggest[2]:
                return
            if x < biggest[2]:
                return
            elif x < biggest[1]:
                biggest[2] = x
            elif x < biggest[0]:
                biggest[2] = biggest[1]
                biggest[1] = x
            else:
                biggest[2] = biggest[1]
                biggest[1] = biggest[0]
                biggest[0] = x

        rows, cols = len(grid), len(grid[0])
        def generate_rhombus(size: int, x: int, y: int):
            if size == 0:
                return grid[x][y]


            # top = (x, y)
            # bottom = (x + 2*size, y)
            # left/right use y +/- size
            if x + 2 * size >= rows or y - size < 0 or y + size >= cols:
                return -1

            total = 0

            # 4 corners
            total += grid[x][y]  # top
            total += grid[x + size][y - size]  # left
            total += grid[x + size][y + size]  # right
            total += grid[x + 2 * size][y]  # bottom

            # edges between corners
            for d in range(1, size):
                total += grid[x + d][y - d]  # top -> left
                total += grid[x + d][y + d]  # top -> right
                total += grid[x + size + d][y - size + d]  # left -> bottom
                total += grid[x + size + d][y + size - d]  # right -> bottom

            return total

        maxSize = min(len(grid) // 2, len(grid[0]) // 2)
        for i in range(maxSize + 1):
            for j in range(len(grid)):
                for k in range(len(grid[0])):
                    compareBiggest(generate_rhombus(i, j, k))
        res = []
        for i in range(3):
            if biggest[i] != -1:
                res.append(biggest[i])
        return res


assert Solution().getBiggestThree(
    [[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]]) == [228, 216, 211], \
    f'Expected: [228,216,211], Received: {Solution().getBiggestThree([[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]])}'
assert Solution().getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [20, 9, 8], \
    f'Expected: [20,9,8], Received: {Solution().getBiggestThree([[1, 2, 3], [4, 5, 6], [7, 8, 9]])}'
assert Solution().getBiggestThree([[7, 7, 7]]) == [7], \
    f'Expected: [7], Received: {Solution().getBiggestThree([[7, 7, 7]])}'
