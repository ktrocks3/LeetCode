import heapq
from typing import List


import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        s = sum(target)
        target = [-x for x in target]
        heapq.heapify(target)

        while True:
            n = -heapq.heappop(target)
            rest = s - n

            # Case 1: already all 1s
            if n == 1 or rest == 1:
                return True

            # Invalid cases
            if rest == 0 or rest >= n:
                return False

            m = n % rest

            # If modulo gives 0 then invalid
            if m == 0:
                return False

            s = rest + m
            heapq.heappush(target, -m)



assert Solution().isPossible([9, 3, 5]) == True, \
    f'Expected: True, Received: {Solution().isPossible([9, 3, 5])}'
assert Solution().isPossible([1, 1, 1, 2]) == False, \
    f'Expected: False, Received: {Solution().isPossible([1, 1, 1, 2])}'
assert Solution().isPossible([1, 1, 2]) == False, \
    f'Expected: False, Received: {Solution().isPossible([1, 1, 2])}'
assert Solution().isPossible([8, 5]) == True, \
    f'Expected: True, Received: {Solution().isPossible([8, 5])}'
