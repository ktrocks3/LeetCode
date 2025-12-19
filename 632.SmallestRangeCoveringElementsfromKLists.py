from typing import List
from collections import deque


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        nums = [deque(l) for l in nums]
        result = ((-1, -1), float('inf'))
        while not any(len(num) == 0 for num in nums):
            low, high = (float('inf'), -1), (-float('inf'), -1)
            for i, num in enumerate(nums):
                if num[0] < low[0]:
                    low = (num[0], i)
                if num[0] > high[0]:
                    high = (num[0], i)
                if high[0] - low[0] < result[1]:
                    result = ((low, high), high[0] - low[0])
            print(low, high)

            nums[0].popleft()

        print(nums)


assert Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20,24], \
  f'Expected: [20,24], Received: {Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]])}'
assert Solution().smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]) == [1,1], \
  f'Expected: [1,1], Received: {Solution().smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]])}'