from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        dp0 = [0 for _ in range(len(nums))]
        dp1, dp2, dp3 = [[-float('inf') for _ in range(len(nums))] for _ in range(3)]
        dp0[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp0[i] = max(nums[i], dp0[i - 1] + nums[i])
                dp1[i] = max(dp1[i - 1] + nums[i], dp0[i - 1] + nums[i])
                dp3[i] = max(dp3[i - 1] + nums[i], dp2[i - 1] + nums[i])
            elif nums[i] < nums[i - 1]:
                dp2[i] = max(dp2[i - 1] + nums[i], dp1[i - 1] + nums[i])
                dp0[i] = nums[i]
            else:
                dp0[i] = nums[i]
        return int(max(dp3))


assert Solution().maxSumTrionic([0, -2, -1, -3, 0, 2, -1]) == -4, \
    f'Expected: -4, Received: {Solution().maxSumTrionic([0, -2, -1, -3, 0, 2, -1])}'
assert Solution().maxSumTrionic([1, 4, 2, 7]) == 14, \
    f'Expected: 14, Received: {Solution().maxSumTrionic([1, 4, 2, 7])}'
