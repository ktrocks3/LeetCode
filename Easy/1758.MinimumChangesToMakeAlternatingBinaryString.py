class Solution:
    def minOperations(self, s: str) -> int:
        diff = 0

        for i in range(len(s)):
            if s[i] != ("1" if i % 2 == 0 else '0'):
                diff += 1

        return min(diff, len(s) - diff)


assert Solution().minOperations('0100') == 1, \
  f'Expected: 1, Received: {Solution().minOperations('0100')}'
assert Solution().minOperations('10') == 0, \
  f'Expected: 0, Received: {Solution().minOperations('10')}'
assert Solution().minOperations('1111') == 2, \
  f'Expected: 2, Received: {Solution().minOperations('1111')}'
