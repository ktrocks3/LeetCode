from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array for range updates

        # Process each query
        for q_up, q_down in queries:
            diff[q_up] -= 1
            if q_down + 1 < n:
                diff[q_down + 1] += 1

        # Apply the difference array to nums
        for i in range(n):
            if i > 0:
                diff[i] += diff[i - 1]
            nums[i] += diff[i]

        # Check if all elements are zero
        return all(x <= 0 for x in nums)


assert Solution().isZeroArray([1, 0, 1], [[0, 2]]) == True
assert Solution().isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]) == False
