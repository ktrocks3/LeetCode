from typing import List


class Solution:
    def largestSubmatrix2(self, matrix: List[List[int]]) -> int:
        # Hint 1: For each column, find the number of consecutive ones ending at each position.
        # Sounds like basically take the prefix sum of matrixT, but reset at 0s
        matrixT = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]  # O(n*m)
        for col in matrixT: # O(n*m)
            for i in range(1, len(col)):
                col[i] = col[i - 1] + 1 if col[i] == 1 else 0
        # Hint 2: For each row, sort the cumulative ones in non-increasing order and "fit" the largest submatrix.
        # So if we transpose it back, we can then sort the rows kinda
        matrix = [[matrixT[i][j] for i in range(len(matrixT))] for j in range(len(matrixT[0]))] # O(n*m)
        print(matrix)
        sorted_matrix = [sorted(row, reverse=True) for row in matrix]
        # Now the area of each item in each row is the minimum height it can achieve, times the index
        area = 0
        for i in range(len(sorted_matrix)):
            for j in range(len(sorted_matrix[0])):
                area = max(area, sorted_matrix[i][j] * (j+1))
        return area
    # That works but I feel like I flipped the matrix twice which is probably unnecessary

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i-1][j] + 1 if matrix[i][j] == 1 else 0
        area = 0
        for row in matrix:
            row.sort(reverse=True)
            for i in range(len(row)):
                area = max(area, row[i] * (i+1))
        return area


assert Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4, \
    f'Expected: 4, Received: {Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]])}'
assert Solution().largestSubmatrix([[1, 0, 1, 0, 1]]) == 3, \
    f'Expected: 3, Received: {Solution().largestSubmatrix([[1, 0, 1, 0, 1]])}'
assert Solution().largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2, \
    f'Expected: 2, Received: {Solution().largestSubmatrix([[1, 1, 0], [1, 0, 1]])}'
