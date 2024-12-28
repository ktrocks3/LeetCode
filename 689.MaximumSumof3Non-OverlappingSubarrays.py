from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Calculate the sum of all k-length subarrays
        n = len(nums)
        k_sum = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        k_sum[0] = current_sum

        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            k_sum[i] = current_sum

        # Step 2: Precompute the best indices for single, double, and triple subarrays
        left = [0] * len(k_sum)
        right = [0] * len(k_sum)

        # Left to right for best single subarray
        best = 0
        for i in range(len(k_sum)):
            if k_sum[i] > k_sum[best]:
                best = i
            left[i] = best

        # Right to left for best single subarray
        best = len(k_sum) - 1
        for i in range(len(k_sum) - 1, -1, -1):
            if k_sum[i] >= k_sum[best]:  # Use >= to maintain lexicographical order
                best = i
            right[i] = best

        # Step 3: Find the best combination of three subarrays
        max_sum = 0
        result = [-1, -1, -1]

        for middle in range(k, len(k_sum) - k):
            l = left[middle - k]
            r = right[middle + k]
            total = k_sum[l] + k_sum[middle] + k_sum[r]

            if total > max_sum:
                max_sum = total
                result = [l, middle, r]

        return result


# Testing
assert Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5], \
    f'Expected: [0,3,5], Received: {Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)}'
assert Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2) == [0, 2, 4], \
    f'Expected: [0,2,4], Received: {Solution().maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2)}'
