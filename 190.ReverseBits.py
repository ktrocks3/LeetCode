class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1
        return result


assert Solution().reverseBits(43261596) == 964176192, \
  f'Expected: 964176192, Received: {Solution().reverseBits(43261596)}'
assert Solution().reverseBits(2147483644) == 1073741822, \
  f'Expected: 1073741822, Received: {Solution().reverseBits(2147483644)}'