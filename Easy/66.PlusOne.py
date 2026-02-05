from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        while pointer >= 0:
            if digits[pointer] == 9:
                digits[pointer] = 0
                pointer -= 1
            else:
                digits[pointer] += 1
                return digits
        return [1] + digits


assert Solution().plusOne([1, 2, 3]) == [1, 2, 4], f"Expected: [1,2,4], Actual: {Solution().plusOne([1, 2, 3])}"
assert Solution().plusOne([4, 3, 2, 1]) == [4, 3, 2, 2], \
    f"Expected: [4,3,2,2], Actual: {Solution().plusOne([4, 3, 2, 1])}"
assert Solution().plusOne([9]) == [1, 0], f"Expected: [1, 0], Actual: {Solution().plusOne([9])}"
