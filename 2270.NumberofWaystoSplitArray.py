from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        running = 0
        res = 0
        for i in range(len(nums)-1):
            running += nums[i]
            total -= nums[i]
            if running >= total:
                res += 1
        return res


assert Solution().waysToSplitArray([10, 4, -8, 7]) == 2, \
    f'Expected: 2, Received: {Solution().waysToSplitArray([10, 4, -8, 7])}'
assert Solution().waysToSplitArray([2, 3, 1, 0]) == 2, \
    f'Expected: 2, Received: {Solution().waysToSplitArray([2, 3, 1, 0])}'
