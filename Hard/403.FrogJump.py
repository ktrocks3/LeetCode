from typing import List

from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # A set for quick lookup of stone positions
        stone_set = set(stones)
        # Memoization dictionary to store already computed results
        memo = {}

        def dfs(position, jump):
            # If we've reached the last stone, return True
            if position == stones[-1]:
                return True
            # If the position is invalid, return False
            if position not in stone_set or jump < 0:
                return False
            # If the current state is already computed, return it
            if (position, jump) in memo:
                return memo[(position, jump)]
            # Try all possible jumps (k-1, k, k+1)
            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0 and dfs(position + next_jump, next_jump):
                    memo[(position, jump)] = True
                    return True
            # Mark this state as not possible and return False
            memo[(position, jump)] = False
            return False

        # Start the DFS from the first jump (1 unit from the first stone)
        if stones[1] != 1 + stones[0]:
            return False
        return dfs(0, 0)


assert Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17]) == True, \
    f'Expected: True, Received: {Solution().canCross([0, 1, 3, 5, 6, 8, 12, 17])}'
assert Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11]) == False, \
    f'Expected: False, Received: {Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])}'
print("Hi")
assert Solution().canCross([0, 1, 2, 5, 6, 9, 10, 12, 13, 14, 17, 19, 20, 21, 26, 27, 28, 29, 30]) == False, \
    f'Expected: False, Received: {Solution().canCross([0, 1, 2, 5, 6, 9, 10, 12, 13, 14, 17, 19, 20, 21, 26, 27, 28, 29, 30])}'
