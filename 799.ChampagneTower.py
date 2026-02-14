class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp[j] = amount of champagne in glass at current row, position j (not capped at 1 yet)
        dp = [0.0] * (query_row + 2)
        dp[0] = float(poured)

        for r in range(query_row):
            next_dp = [0.0] * (query_row + 2)
            for j in range(r + 1):
                excess = max(0.0, dp[j] - 1.0)
                if excess > 0:
                    next_dp[j] += excess / 2.0
                    next_dp[j + 1] += excess / 2.0
            dp = next_dp

        return min(1.0, dp[query_glass])


assert Solution().champagneTower(1, 1, 1) == 0.00000, \
    f'Expected: 0.00000, Received: {Solution().champagneTower(1, 1, 1)}'
assert Solution().champagneTower(2, 1, 1) == 0.50000, \
    f'Expected: 0.50000, Received: {Solution().champagneTower(2, 1, 1)}'
assert Solution().champagneTower(100000009, 33, 17) == 1.00000, \
    f'Expected: 1.00000, Received: {Solution().champagneTower(100000009, 33, 17)}'
