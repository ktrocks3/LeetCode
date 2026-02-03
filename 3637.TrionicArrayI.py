from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return False
            b = nums[i] > nums[i-1]
            if len(increasing) == 0 or increasing[-1] != b:
                increasing.append(b)
        return increasing == [True, False, True]





assert Solution().isTrionic([1, 3, 5, 4, 2, 6]) == True, \
  f'Expected: True, Received: {Solution().isTrionic([1, 3, 5, 4, 2, 6])}'
assert Solution().isTrionic([2, 1, 3]) == False, \
  f'Expected: False, Received: {Solution().isTrionic([2, 1, 3])}'