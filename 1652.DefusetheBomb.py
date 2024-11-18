from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n

        res = [0] * n
        code_extended = code * 2  # Extend the code for easier index wrapping

        if k > 0:
            # Initialize the sliding window sum for the first position
            window_sum = sum(code_extended[1:k + 1])
            for i in range(n):
                res[i] = window_sum
                # Slide the window to the next position
                window_sum += code_extended[i + k + 1] - code_extended[i + 1]
        else:  # k < 0
            # Initialize the sliding window sum for the first position
            window_sum = sum(code_extended[n + k:n])
            for i in range(n):
                res[i] = window_sum
                # Slide the window to the next position
                window_sum += code_extended[n + i] - code_extended[n + i + k]

        return res


assert Solution().decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert Solution().decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert Solution().decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
