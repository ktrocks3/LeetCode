from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if len(nums) - i <= ans:
                break
            freq = {}
            even_odd = 0
            for j in range(i, len(nums)):
                freq[nums[j]] = freq.get(nums[j], 0) + 1
                if freq[nums[j]] == 1:
                    if nums[j] % 2 == 1:
                        even_odd += 1
                    else:
                        even_odd -= 1
                if even_odd == 0:
                    ans = max(ans, j - i + 1)
        return ans


assert Solution().longestBalanced([2, 5, 4, 3]) == 4, \
    f'Expected: 4, Received: {Solution().longestBalanced([2, 5, 4, 3])}'
assert Solution().longestBalanced([3, 2, 2, 5, 4]) == 5, \
    f'Expected: 5, Received: {Solution().longestBalanced([3, 2, 2, 5, 4])}'
assert Solution().longestBalanced([1, 2, 3, 2]) == 3, \
    f'Expected: 3, Received: {Solution().longestBalanced([1, 2, 3, 2])}'
