class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_mask = 0
        for p in (2, 3, 5, 7, 11, 13, 17, 19):
            prime_mask |= 1 << p

        ans = 0
        for num in range(left, right + 1):
            ans += (prime_mask >> num.bit_count()) & 1
        return ans


assert Solution().countPrimeSetBits(6, 10) == 4, \
    f'Expected: 4, Received: {Solution().countPrimeSetBits(6, 10)}'
assert Solution().countPrimeSetBits(10, 15) == 5, \
    f'Expected: 5, Received: {Solution().countPrimeSetBits(10, 15)}'
