from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # Count reverse pairs
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                self.count += j

            # Merge step
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged

        merge_sort(nums)
        return self.count


assert Solution().reversePairs([1, 3, 2, 3, 1]) == 2, \
    f'Expected: 2, Received: {Solution().reversePairs([1, 3, 2, 3, 1])}'
assert Solution().reversePairs([2, 4, 3, 5, 1]) == 3, \
    f'Expected: 3, Received: {Solution().reversePairs([2, 4, 3, 5, 1])}'
