from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        # Step 1: Create mismatch array
        mismatch = [0] * n
        for i in range(1, n):
            mismatch[i] = 1 if nums[i] % 2 == nums[i - 1] % 2 else 0

        # Step 2: Build prefix sum of mismatch array
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + mismatch[i - 1]

        # Step 3: Answer queries
        res = []
        for start, end in queries:
            # Check for mismatches in the range [start, end]
            if prefix[end + 1] - prefix[start + 1] > 0:
                res.append(False)
            else:
                res.append(True)

        return res


assert Solution().isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]) == [False], \
    f'Expected: [false], Received: {Solution().isArraySpecial([3, 4, 1, 2, 6], [[0, 4]])}'
assert Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]) == [False, True], \
    f'Expected: , Received: {Solution().isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]])}'
assert Solution().isArraySpecial([6,4,9], [[0, 2]]) == [False], \
    f'Expected: , Received: {Solution().isArraySpecial([6,4,9], [[0, 2]])}'
