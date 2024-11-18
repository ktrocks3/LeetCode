from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1

        # Find the leftmost sorted part
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        # If the whole array is sorted
        if left == n - 1:
            return 0

        # Find the rightmost sorted part
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        # Calculate the minimum length to remove
        # Option 1: Remove all from the left or all from the right
        result = min(n - left - 1, right)

        # Option 2: Merge sorted left and right parts
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j - i - 1)
                i += 1
            else:
                j += 1

        return result

# Test cases
assert Solution().findLengthOfShortestSubarray([1, 2, 3, 10, 4, 2, 3, 5]) == 3
assert Solution().findLengthOfShortestSubarray([5, 4, 3, 2, 1]) == 4
assert Solution().findLengthOfShortestSubarray([1, 2, 3]) == 0
assert Solution().findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1]) == 3
