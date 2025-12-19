from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [nums[0]]
        for n in nums[1:]:
            prefix.append(n + prefix[-1])
        l = len(nums) // k
        besti, bestk, bestval = 0, 0, 0
        for i in range(len(prefix)):
            for h in range(l):
                print(prefix[i:i+(k*h)+1])


assert Solution().maxSubarraySum([1, 2], 1) == 3, \
    f'Expected: 3, Received: {Solution().maxSubarraySum([1, 2], 1)}'
assert Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4) == -10, \
    f'Expected: -10, Received: {Solution().maxSubarraySum([-1, -2, -3, -4, -5], 4)}'
assert Solution().maxSubarraySum([-5, 1, 2, -3, 4], 2) == 4, \
    f'Expected: 4, Received: {Solution().maxSubarraySum([-5, 1, 2, -3, 4], 2)}'
