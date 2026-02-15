import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not a or not b:
            return 1 if b == "" else -1

        k = math.ceil(len(b)/len(a))
        s = a * k
        if b in s:
            return k
        s = a * (k + 1)
        if b in s:
            return k + 1
        return -1



assert Solution().repeatedStringMatch('abcd', 'cdabcdab') == 3, \
  f'Expected: 3, Received: {Solution().repeatedStringMatch('abcd', 'cdabcdab')}'
assert Solution().repeatedStringMatch('a', 'aa') == 2, \
  f'Expected: 2, Received: {Solution().repeatedStringMatch('a', 'aa')}'