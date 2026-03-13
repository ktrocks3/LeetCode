from typing import List

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[start] <= nums[mid]:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1



assert Solution().search([4, 5, 6, 7, 0, 1, 2], 0) == 4, \
  f'Expected: 4, Received: {Solution().search([4, 5, 6, 7, 0, 1, 2], 0)}'
assert Solution().search([4, 5, 6, 7, 0, 1, 2], 3) == -1, \
  f'Expected: -1, Received: {Solution().search([4, 5, 6, 7, 0, 1, 2], 3)}'
assert Solution().search([1], 0) == -1, \
  f'Expected: -1, Received: {Solution().search([1], 0)}'