class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        s = int(s, 2)
        while s > 1:
            if s % 2 == 0:
                s = s // 2
            else:
                s += 1
            steps += 1
        return steps

assert Solution().numSteps('1101') == 6, \
  f'Expected: 6, Received: {Solution().numSteps('1101')}'
assert Solution().numSteps('10') == 1, \
  f'Expected: 1, Received: {Solution().numSteps('10')}'
assert Solution().numSteps('1') == 0, \
  f'Expected: 0, Received: {Solution().numSteps('1')}'
