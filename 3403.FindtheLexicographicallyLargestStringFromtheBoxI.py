class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
        l = n - numFriends + 1
        best = ""
        for i in range(n):
            candidate = word[i : i + l]
            if candidate > best:
                best = candidate

        return best


# Tests
assert Solution().answerString("dbca", 2) == "dbc", \
    f'Expected: "dbc", Received: {Solution().answerString("dbca", 2)}'
assert Solution().answerString("gggg", 4) == "g", \
    f'Expected: "g", Received: {Solution().answerString("gggg", 4)}'
assert Solution().answerString("gh", 1) == "gh", \
    f'Expected: "gh", Received: {Solution().answerString("gh", 1)}'
