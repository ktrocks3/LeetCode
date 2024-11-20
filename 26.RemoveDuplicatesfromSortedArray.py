from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 1
        for i in range(1, len(nums)):
            if (nums[i] != nums[i - 1]):
                nums[count] = nums[i]
                count += 1
        return count


x = [1, 1, 2]
Solution().removeDuplicates(x)
assert x[:2] == [1, 2]

x = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Solution().removeDuplicates(x)
assert x[:5] == [0, 1, 2, 3, 4]
