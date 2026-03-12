from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1


assert Solution().search([-1, 0, 3, 5, 9, 12], 9) == 4, \
  f'Expected: 4, Received: {Solution().search([-1, 0, 3, 5, 9, 12], 9)}'
assert Solution().search([-1, 0, 3, 5, 9, 12], 2) == -1, \
  f'Expected: -1, Received: {Solution().search([-1, 0, 3, 5, 9, 12], 2)}'
