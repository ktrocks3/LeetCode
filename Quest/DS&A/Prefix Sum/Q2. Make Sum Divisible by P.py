from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)

        total = sum(nums)

        if total < p:
            return -1

        total %= p
        if total == 0:
            return 0

        for num in nums:
            if num % p == total:
                return 1

        last_seen = {0: 0}
        min_size = n
        curr = 0

        for i, num in enumerate(nums):
            curr = (curr + num) % p
            target = curr - total
            if target < 0:
                target += p

            if target in last_seen:
                size = i + 1 - last_seen[target]
                if size < min_size:
                    min_size = size

            last_seen[curr] = i + 1

        return min_size if min_size < n else -1


assert Solution().minSubarray([3, 1, 4, 2], 6) == 1, \
    f'Expected: 1, Received: {Solution().minSubarray([3, 1, 4, 2], 6)}'
assert Solution().minSubarray([6, 3, 5, 2], 9) == 2, \
    f'Expected: 2, Received: {Solution().minSubarray([6, 3, 5, 2], 9)}'
assert Solution().minSubarray([1, 2, 3], 3) == 0, \
    f'Expected: 0, Received: {Solution().minSubarray([1, 2, 3], 3)}'
