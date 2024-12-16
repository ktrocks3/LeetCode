from typing import List
from heapq import heappop, heappush, heapify

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums = [(x,i) for i,x in enumerate(nums)]
        heapify(nums)
        for _ in range(k):
            n, i = heappop(nums)
            heappush(nums, (n*multiplier, i))
        return [x for x, _ in sorted(nums, key=lambda x: x[1])]


assert Solution().getFinalState([2, 1, 3, 5, 6], 5, 2) == [8,4,6,5,6], \
  f'Expected: [8,4,6,5,6], Received: {Solution().getFinalState([2, 1, 3, 5, 6], 5, 2)}'
assert Solution().getFinalState([1, 2], 3, 4) == [16,8], \
  f'Expected: [16,8], Received: {Solution().getFinalState([1, 2], 3, 4)}'
