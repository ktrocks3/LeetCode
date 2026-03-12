from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start, end = 0, len(arr) - 1
        while start < end:
            mid = (start + end) // 2
            if arr[mid] > arr[mid+1]:
                end = mid
            else:
                start = mid + 1

        return start

assert Solution().peakIndexInMountainArray([0, 1, 0]) == 1, \
  f'Expected: 1, Received: {Solution().peakIndexInMountainArray([0, 1, 0])}'
assert Solution().peakIndexInMountainArray([0, 2, 1, 0]) == 1, \
  f'Expected: 1, Received: {Solution().peakIndexInMountainArray([0, 2, 1, 0])}'
assert Solution().peakIndexInMountainArray([0, 10, 5, 2]) == 1, \
  f'Expected: 1, Received: {Solution().peakIndexInMountainArray([0, 10, 5, 2])}'
