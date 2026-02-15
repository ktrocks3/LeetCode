class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


assert Solution().repeatedSubstringPattern('abab') == True, \
    f'Expected: True, Received: {Solution().repeatedSubstringPattern('abab')}'
assert Solution().repeatedSubstringPattern('aba') == False, \
    f'Expected: False, Received: {Solution().repeatedSubstringPattern('aba')}'
assert Solution().repeatedSubstringPattern('abcabcabcabc') == True, \
    f'Expected: True, Received: {Solution().repeatedSubstringPattern('abcabcabcabc')}'
