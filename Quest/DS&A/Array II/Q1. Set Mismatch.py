from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        total = sum(range(1, len(nums) + 1))
        seen = set()
        duplicate = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                duplicate = num
                break
        return [duplicate, total - sum(nums) + duplicate]



assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3], \
    f'Expected: [2,3], Received: {Solution().findErrorNums([1, 2, 2, 4])}'
assert Solution().findErrorNums([1, 1]) == [1, 2], \
    f'Expected: [1,2], Received: {Solution().findErrorNums([1, 1])}'
