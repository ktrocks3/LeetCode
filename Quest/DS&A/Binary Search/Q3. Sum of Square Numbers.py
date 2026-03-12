from math import sqrt, ceil


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start, end = 0, ceil(sqrt(c))
        while start <= end:
            s = start * start + end * end
            if s == c:
                return True
            if s < c:
                start += 1
            if s > c:
                end -= 1
        return False


assert Solution().judgeSquareSum(5) == True, \
  f'Expected: True, Received: {Solution().judgeSquareSum(5)}'
assert Solution().judgeSquareSum(3) == False, \
  f'Expected: False, Received: {Solution().judgeSquareSum(3)}'
