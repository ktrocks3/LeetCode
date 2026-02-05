from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums = nums[1:]
        min1 = float('inf')
        min2 = float('inf')

        for x in nums:
            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        return first + min1 + min2


assert Solution().minimumCost([1, 2, 3, 12]) == 6, \
  f'Expected: 6, Received: {Solution().minimumCost([1, 2, 3, 12])}'
assert Solution().minimumCost([5, 4, 3]) == 12, \
  f'Expected: 12, Received: {Solution().minimumCost([5, 4, 3])}'
assert Solution().minimumCost([10, 3, 1, 1]) == 12, \
  f'Expected: 12, Received: {Solution().minimumCost([10, 3, 1, 1])}'
