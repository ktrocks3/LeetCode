class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = {0: 1}
        mask = 0
        result = 0
        for char in word:
            mask ^= 1 << (ord(char) - ord('a'))
            # Case 1: Check if the mask itself has appeared before
            result += count.get(mask, 0)

            # Case 2: Check masks differing by exactly one bit
            for i in range(10):
                result += count.get(mask ^ (1 << i), 0)

            # Update the count of the current mask
            count[mask] = count.get(mask, 0) + 1

        return result


assert Solution().wonderfulSubstrings('aba') == 4, \
    f'Expected: 4, Received: {Solution().wonderfulSubstrings('aba')}'
assert Solution().wonderfulSubstrings('aabb') == 9, \
    f'Expected: 9, Received: {Solution().wonderfulSubstrings('aabb')}'
assert Solution().wonderfulSubstrings('he') == 2, \
  f'Expected: 2, Received: {Solution().wonderfulSubstrings('he')}'