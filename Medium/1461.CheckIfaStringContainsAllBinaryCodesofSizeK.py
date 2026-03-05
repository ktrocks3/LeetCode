class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        substrings = set()
        for i in range(len(s)-k+1):
            substrings.add(s[i:i+k])
        return len(substrings) == 2 ** k


assert Solution().hasAllCodes('00110110', 2) == True, \
  f'Expected: True, Received: {Solution().hasAllCodes('00110110', 2)}'
assert Solution().hasAllCodes('0110', 1) == True, \
  f'Expected: True, Received: {Solution().hasAllCodes('0110', 1)}'
assert Solution().hasAllCodes('0110', 2) == False, \
  f'Expected: False, Received: {Solution().hasAllCodes('0110', 2)}'
