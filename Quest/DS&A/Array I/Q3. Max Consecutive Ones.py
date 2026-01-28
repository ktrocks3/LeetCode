from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0
        running = 0
        for num in nums:
            if num == 1:
                running += 1
                m = max(m, running)
            else:
                running = 0
        return m



assert Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3, \
  f'Expected: 3, Received: {Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])}'
assert Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2, \
  f'Expected: 2, Received: {Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])}'