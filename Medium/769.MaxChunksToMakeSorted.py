from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_seen = 0
        chunks = 0

        for i, value in enumerate(arr):
            max_seen = max(max_seen, value)
            # A chunk can be created when the maximum value seen so far equals the current index
            if max_seen == i:
                chunks += 1

        return chunks


assert Solution().maxChunksToSorted([4, 3, 2, 1, 0]) == 1, \
    f'Expected: 1, Received: {Solution().maxChunksToSorted([4, 3, 2, 1, 0])}'
assert Solution().maxChunksToSorted([1, 0, 2, 3, 4]) == 4, \
    f'Expected: 4, Received: {Solution().maxChunksToSorted([1, 0, 2, 3, 4])}'
