from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res

assert Solution().shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7], \
    f'Expected: [2,3,5,4,1,7], Received: {Solution().shuffle([2, 5, 1, 3, 4, 7], 3)}'
assert Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1], \
    f'Expected: [1,4,2,3,3,2,4,1], Received: {Solution().shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4)}'
assert Solution().shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2], \
    f'Expected: [1,2,1,2], Received: {Solution().shuffle([1, 1, 2, 2], 2)}'
