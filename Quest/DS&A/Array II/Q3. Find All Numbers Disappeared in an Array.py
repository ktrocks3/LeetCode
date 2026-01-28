from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Method 1:
        # n = len(nums)
        # nums = set(nums)
        # return [x for x in range(1,n+1) if x not in nums]

        # Method 2: In place method using marking :D
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        return [i + 1 for i, v in enumerate(nums) if v > 0]



assert Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5,6], \
  f'Expected: [5,6], Received: {Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])}'
assert Solution().findDisappearedNumbers([1, 1]) == [2], \
  f'Expected: [2], Received: {Solution().findDisappearedNumbers([1, 1])}'