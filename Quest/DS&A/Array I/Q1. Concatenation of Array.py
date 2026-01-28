from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Trivial solution
        return nums + nums
        # Actual solution
        res = []
        for _ in range(2):
            for num in nums:
                res.append(num)
        return res


assert Solution().getConcatenation([1, 2, 1]) == [1,2,1,1,2,1], \
  f'Expected: [1,2,1,1,2,1], Received: {Solution().getConcatenation([1, 2, 1])}'
assert Solution().getConcatenation([1, 3, 2, 1]) == [1,3,2,1,1,3,2,1], \
  f'Expected: [1,3,2,1,1,3,2,1], Received: {Solution().getConcatenation([1, 3, 2, 1])}'
