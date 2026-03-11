from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = nums[len(nums) // 2]
        smaller, larger, equal = [], [], []
        for n in nums:
            if n < pivot:
                smaller.append(n)
            elif n > pivot:
                larger.append(n)
            else:
                equal.append(n)

        if k <= len(larger):
            return self.findKthLargest(larger, k)
        elif k <= len(larger) + len(equal):
            return pivot
        else:
            return self.findKthLargest(smaller, k - len(larger) - len(equal))


assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5, \
    f'Expected: 5, Received: {Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)}'
assert Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4, \
    f'Expected: 4, Received: {Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)}'
