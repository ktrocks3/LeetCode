class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)
        for i in range(len(n) - 1):
            if n[i] == n[i + 1]:
                return False
        return True

assert Solution().hasAlternatingBits(5) == True, \
  f'Expected: True, Received: {Solution().hasAlternatingBits(5)}'
assert Solution().hasAlternatingBits(7) == False, \
  f'Expected: False, Received: {Solution().hasAlternatingBits(7)}'
assert Solution().hasAlternatingBits(11) == False, \
  f'Expected: False, Received: {Solution().hasAlternatingBits(11)}'
