from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # Really easy, if there's an even amount it's all positive, if it's odd, it's the smallest negative subtracted
        # Doesn't even have to be a grid
        res = []
        for row in matrix:
            res.extend(row)
        even = True
        smallest = 1000000
        total = 0
        for val in res:
            if val < 0:
                even = not even
            smallest = min(smallest, abs(val))
            total += abs(val)


        return total if even else total - (2 * smallest)


assert Solution().maxMatrixSum([[1, -1], [-1, 1]]) == 4
assert Solution().maxMatrixSum([[1, 2, 3], [-1, -2, -3], [1, 2, 3]]) == 16
assert Solution().maxMatrixSum([[2, 9, 3], [5, 4, -4], [1, 7, 1]]) == 34
