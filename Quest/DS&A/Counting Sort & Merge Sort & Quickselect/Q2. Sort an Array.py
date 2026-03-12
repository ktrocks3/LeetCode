from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        half = len(nums) // 2
        half1 = self.sortArray(nums[:half])
        half2 = self.sortArray(nums[half:])

        res = []
        i = j = 0

        while i < len(half1) and j < len(half2):
            if half1[i] <= half2[j]:
                res.append(half1[i])
                i += 1
            else:
                res.append(half2[j])
                j += 1

        res.extend(half1[i:])
        res.extend(half2[j:])

        return res

assert Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5], \
    f'Expected: [1,2,3,5], Received: {Solution().sortArray([5, 2, 3, 1])}'
assert Solution().sortArray([5, 1, 1, 2, 0, 0]) == [0, 0, 1, 1, 2, 5], \
    f'Expected: [0,0,1,1,2,5], Received: {Solution().sortArray([5, 1, 1, 2, 0, 0])}'
