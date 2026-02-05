from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        # Check if the problem is solvable
        if (target + total_sum) % 2 != 0 or target > total_sum:
            return 0

        subset_sum = (target + total_sum) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to get a sum of 0: use no elements

        for num in nums:
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]


assert Solution().findTargetSumWays([1, 1, 1, 1, 1], 3) == 5, \
  f'Expected: 5, Received: {Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)}'
assert Solution().findTargetSumWays([1], 1) == 1, \
  f'Expected: 1, Received: {Solution().findTargetSumWays([1], 1)}'