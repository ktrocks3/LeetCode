from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        arr = [1]
        while len(arr) < n:
            even = [2 * x for x in arr if 2 * x <= n]
            odd = [2 * x - 1 for x in arr if 2 * x - 1 <= n]
            arr = odd + even
        return arr