class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


assert Solution().rotateString('abcde', 'cdeab') == True, \
  f'Expected: True, Received: {Solution().rotateString('abcde', 'cdeab')}'
assert Solution().rotateString('abcde', 'abced') == False, \
  f'Expected: False, Received: {Solution().rotateString('abcde', 'abced')}'
assert Solution().rotateString('aa', 'a') == False, \
  f'Expected: False, Received: {Solution().rotateString('aa', 'a')}'
