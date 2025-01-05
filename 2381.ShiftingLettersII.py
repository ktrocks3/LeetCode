from collections import defaultdict
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)  # Difference array

        # Apply difference array technique
        for start, end, direction in shifts:
            delta[start] += 1 if direction else -1
            delta[end + 1] -= 1 if direction else -1

        # Compute prefix sum to get the net shift for each character
        net_shift = 0
        for i in range(n):
            net_shift += delta[i]
            delta[i] = net_shift

        # Apply shifts to the string
        res = []
        for i in range(n):
            x = ord(s[i]) + delta[i]
            x = (x - ord('a')) % 26 + ord('a')  # Wrap around within 'a' to 'z'
            res.append(chr(x))

        return ''.join(res)



assert Solution().shiftingLetters('abc', [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace", \
    f'Expected: "ace", Received: {Solution().shiftingLetters('abc', [[0, 1, 0], [1, 2, 1], [0, 2, 1]])}'
assert Solution().shiftingLetters('dztz', [[0, 0, 0], [1, 1, 1]]) == "catz", \
    f'Expected: "catz", Received: {Solution().shiftingLetters('dztz', [[0, 0, 0], [1, 1, 1]])}'
