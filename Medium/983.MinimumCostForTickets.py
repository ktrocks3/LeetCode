from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days = set(days)
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 30)] + costs[2])
        return dp[-1]


assert Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11, \
  f'Expected: 11, Received: {Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])}'
assert Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]) == 17, \
  f'Expected: 17, Received: {Solution().mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])}'