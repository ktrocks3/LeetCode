class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


assert Solution().lengthOfLastWord("Hello World") == 5, \
    f"Expected: 5, Actual: {Solution().lengthOfLastWord("Hello World")}"
assert Solution().lengthOfLastWord("   fly me   to   the moon  ") == 4, \
    f"Expected: 4, Actual: {Solution().lengthOfLastWord("   fly me   to   the moon  ")}"
assert Solution().lengthOfLastWord("luffy is still joyboy") == 6, \
    f"Expected: 6, Actual: {Solution().lengthOfLastWord("luffy is still joyboy")}"
