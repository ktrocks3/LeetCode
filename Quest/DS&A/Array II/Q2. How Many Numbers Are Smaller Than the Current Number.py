from collections import defaultdict
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        count = []
        res = []
        total = 0
        for i in range(max(hm)+1):
            count.append(total)
            total += hm.get(i, 0)

        for num in nums:
            res.append(count[num])
        return res


assert Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4,0,1,1,3], \
  f'Expected: [4,0,1,1,3], Received: {Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3])}'
assert Solution().smallerNumbersThanCurrent([6, 5, 4, 8]) == [2,1,0,3], \
  f'Expected: [2,1,0,3], Received: {Solution().smallerNumbersThanCurrent([6, 5, 4, 8])}'
assert Solution().smallerNumbersThanCurrent([7, 7, 7, 7]) == [0,0,0,0], \
  f'Expected: [0,0,0,0], Received: {Solution().smallerNumbersThanCurrent([7, 7, 7, 7])}'