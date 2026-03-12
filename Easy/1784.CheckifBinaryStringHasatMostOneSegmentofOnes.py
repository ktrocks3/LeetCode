class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        seenOne = False
        seenZeroAfterOne = False
        for c in s:
            if c == '1' and not seenOne:
                seenOne = True
            if c == '0' and not seenZeroAfterOne and seenOne:
                seenZeroAfterOne = True
            if seenZeroAfterOne and c == '1':
                return False
        return seenOne


assert Solution().checkOnesSegment('1001') == False, \
  f'Expected: False, Received: {Solution().checkOnesSegment('1001')}'
assert Solution().checkOnesSegment('110') == True, \
  f'Expected: True, Received: {Solution().checkOnesSegment('110')}'
