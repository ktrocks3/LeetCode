class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        c_old = [0]*26
        for c in s:
            c_old[ord(c)-97] += 1
        c = [0] * 26

        while t:
            c = [0] * 26
            for i in range(26):
                if i == 25:
                    c[0] += c_old[i] % (10**9 + 7)
                    c[1] += c_old[i] % (10**9 + 7)
                else:
                    c[i+1] += c_old[i] % (10**9 + 7)
            t -= 1
            c_old = c
        return sum(c) % (10**9 + 7)

assert Solution().lengthAfterTransformations('abcyy', 2) == 7, \
  f'Expected: 7, Received: {Solution().lengthAfterTransformations('abcyy', 2)}'
assert Solution().lengthAfterTransformations('azbk', 1) == 5, \
  f'Expected: 5, Received: {Solution().lengthAfterTransformations('azbk', 1)}'
assert Solution().lengthAfterTransformations('cu', 5) == 2, \
  f'Expected: 2, Received: {Solution().lengthAfterTransformations('cu', 1)}'
assert Solution().lengthAfterTransformations('jqktcurgdvlibczdsvnsg', 7517) == 79033769, \
  f'Expected: 2, Received: {Solution().lengthAfterTransformations('jqktcurgdvlibczdsvnsg', 7517)}'