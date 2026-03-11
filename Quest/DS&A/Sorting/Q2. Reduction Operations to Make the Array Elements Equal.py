from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        operations = 0
        count = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                count += 1
            operations += count
        return operations



assert Solution().reductionOperations([5, 1, 3]) == 3, \
  f'Expected: 3, Received: {Solution().reductionOperations([5, 1, 3])}'
assert Solution().reductionOperations([1, 1, 1]) == 0, \
  f'Expected: 0, Received: {Solution().reductionOperations([1, 1, 1])}'
assert Solution().reductionOperations([1, 1, 2, 2, 3]) == 4, \
  f'Expected: 4, Received: {Solution().reductionOperations([1, 1, 2, 2, 3])}'