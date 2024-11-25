import copy
from typing import List, Tuple
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Target goal
        goal = [[1, 2, 3], [4, 5, 0]]

        # Convert board to tuple for immutability
        def board_to_tuple(b):
            return tuple(tuple(row) for row in b)

        # Movement helper functions
        def move(x, y, dx, dy, b):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < 3:  # Ensure within bounds
                b[x][y], b[nx][ny] = b[nx][ny], b[x][y]  # Swap
                return board_to_tuple(b)
            return None

        # Generate possible moves
        def moves(b):
            b = [list(row) for row in b]  # Convert tuple back to list
            x, y = next((i, row.index(0)) for i, row in enumerate(b) if 0 in row)  # Locate zero
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
            return [move(x, y, dx, dy, copy.deepcopy(b)) for dx, dy in directions]

        # BFS
        queue = deque([(board_to_tuple(board), 0)])
        seen = set()
        seen.add(board_to_tuple(board))

        while queue:
            state, depth = queue.popleft()
            if state == board_to_tuple(goal):
                return depth

            for next_state in moves(state):
                if next_state and next_state not in seen:
                    queue.append((next_state, depth + 1))
                    seen.add(next_state)

        return -1  # Return -1 if unsolvable


# Testing
assert Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5, \
    f"Expected 5, received {Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])}"

assert Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1, \
    f"Expected 1, received {Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]])}"

assert Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1, \
    f"Expected -1, received {Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]])}"
