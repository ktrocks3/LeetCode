class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)[2:]
        res = []
        for c in n:
            res.append('0' if c == '1' else '1')
        res = ''.join(res)
        return int(res, 2)



assert Solution().bitwiseComplement(5) == 2, \
  f'Expected: 2, Received: {Solution().bitwiseComplement(5)}'
assert Solution().bitwiseComplement(7) == 0, \
  f'Expected: 0, Received: {Solution().bitwiseComplement(7)}'
assert Solution().bitwiseComplement(10) == 5, \
  f'Expected: 5, Received: {Solution().bitwiseComplement(10)}'