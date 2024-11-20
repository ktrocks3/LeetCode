from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


x = [3, 2, 2, 3]
assert Solution().removeElement(x, 3) == 2
assert x[:2] == [2, 2]

x = [0, 1, 2, 2, 3, 0, 4, 2]
assert Solution().removeElement(x, 2) == 5
assert x[:5] == [0, 1, 3, 0, 4]
