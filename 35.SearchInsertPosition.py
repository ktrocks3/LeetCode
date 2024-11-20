from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low


assert Solution().searchInsert([1, 3, 5, 6], 5) == 2, \
    f'Expected 2, recieved {Solution().searchInsert([1, 3, 5, 6], 5)}'
assert Solution().searchInsert([1, 3, 5, 6], 2) == 1, \
    f'Expected 1, recieved {Solution().searchInsert([1, 3, 5, 6], 2)}'
assert Solution().searchInsert([1, 3, 5, 6], 7) == 4, \
    f'Expected 4, recieved {Solution().searchInsert([1, 3, 5, 6], 4)}'
