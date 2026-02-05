from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i + nums[i]) % len(nums)] for i in range(len(nums))]


assert Solution().constructTransformedArray([3, -2, 1, 1]) == [1,1,1,3], \
  f'Expected: [1,1,1,3], Received: {Solution().constructTransformedArray([3, -2, 1, 1])}'
assert Solution().constructTransformedArray([-1, 4, -1]) == [-1,-1,4], \
  f'Expected: [-1,-1,4], Received: {Solution().constructTransformedArray([-1, 4, -1])}'