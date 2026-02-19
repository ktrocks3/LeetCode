from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            v = nums[i]
            if 1 <= v <= n and nums[v - 1] != v:
                nums[v - 1], nums[i] = nums[i], nums[v - 1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


class Solution2:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set([x for x in nums if x > 0])
        if not nums:
            return 1
        for i in range(1, max(nums) + 2):
            if i not in nums:
                return i
        return -1


assert Solution().firstMissingPositive([1, 2, 0]) == 3, \
    f'Expected: 3, Received: {Solution().firstMissingPositive([1, 2, 0])}'
assert Solution().firstMissingPositive([3, 4, -1, 1]) == 2, \
    f'Expected: 2, Received: {Solution().firstMissingPositive([3, 4, -1, 1])}'
assert Solution().firstMissingPositive([7, 8, 9, 11, 12]) == 1, \
    f'Expected: 1, Received: {Solution().firstMissingPositive([7, 8, 9, 11, 12])}'
