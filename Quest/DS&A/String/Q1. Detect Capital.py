class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

assert Solution().detectCapitalUse('USA') == True, \
    f'Expected: True, Received: {Solution().detectCapitalUse('USA')}'
assert Solution().detectCapitalUse('FlaG') == False, \
    f'Expected: False, Received: {Solution().detectCapitalUse('FlaG')}'
