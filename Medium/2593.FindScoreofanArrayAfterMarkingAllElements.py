import heapq
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Create a min-heap with (value, index)
        heap = [(nums[i], i) for i in range(len(nums))]
        heapq.heapify(heap)

        score = 0
        marked = [False] * len(nums)  # Keep track of marked indices

        while heap:
            value, index = heapq.heappop(heap)  # Get the smallest element
            if marked[index]:  # Skip if already marked
                continue

            score += value
            # Mark the current index and its neighbors
            if index > 0:
                marked[index - 1] = True
            marked[index] = True
            if index < len(nums) - 1:
                marked[index + 1] = True

        return score


assert Solution().findScore([2, 1, 3, 4, 5, 2]) == 7, \
    f'Expected: 7, Received: {Solution().findScore([2, 1, 3, 4, 5, 2])}'
assert Solution().findScore([2, 3, 5, 1, 3, 2]) == 5, \
    f'Expected: 5, Received: {Solution().findScore([2, 3, 5, 1, 3, 2])}'
