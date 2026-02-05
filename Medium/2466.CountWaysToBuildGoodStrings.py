class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0 for _ in range(high + 1)]
        dp[0] = 1  # Base case: one way to create an empty string

        for i in range(1, high + 1):
            if (i - zero) >= 0:
                dp[i] += dp[i - zero]
            if (i - one) >= 0:
                dp[i] += dp[i - one]
            dp[i] %= MOD  # Take modulo at each step

        result = sum(dp[low:high + 1]) % MOD

        return result

assert Solution().countGoodStrings(3, 3, 1, 1) == 8, \
  f'Expected: 8, Received: {Solution().countGoodStrings(3, 3, 1, 1)}'
assert Solution().countGoodStrings(2, 3, 1, 2) == 5, \
  f'Expected: 5, Received: {Solution().countGoodStrings(2, 3, 1, 2)}'
