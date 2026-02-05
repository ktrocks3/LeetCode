from typing import List

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        if not values:
            return 0
        max_i = values[0]  # Initialize max_i as values[0] + 0 since i = 0
        max_score = float('-inf')  # Start with a very low value

        for j in range(1, len(values)):
            # Calculate the score for the pair (i, j)
            max_score = max(max_score, max_i + values[j] - j)

            # Update max_i to include the current element
            max_i = max(max_i, values[j] + j)

        return max_score if max_score > float('-inf') else 0


assert Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11, \
    f'Expected: 11, Received: {Solution().maxScoreSightseeingPair([8, 1, 5, 2, 6])}'
assert Solution().maxScoreSightseeingPair([1, 2]) == 2, \
    f'Expected: 2, Received: {Solution().maxScoreSightseeingPair([1, 2])}'
assert Solution().maxScoreSightseeingPair([1]) == 0, \
    f'Expected: 0, Received: {Solution().maxScoreSightseeingPair([1])}'
assert Solution().maxScoreSightseeingPair([]) == 0, \
    f'Expected: 0, Received: {Solution().maxScoreSightseeingPair([])}'
