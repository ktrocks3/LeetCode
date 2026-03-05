class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        cnt = 0
        start = 0

        for i, ch in enumerate(s):
            cnt += 1 if ch == '1' else -1
            if cnt == 0:
                # s[start:i+1] is a primitive special substring: 1 + inner + 0
                inner = s[start + 1:i]
                parts.append('1' + self.makeLargestSpecial(inner) + '0')
                start = i + 1

        parts.sort(reverse=True)
        return ''.join(parts)



assert Solution().makeLargestSpecial('11011000') == "11100100", \
    f'Expected: "11100100", Received: {Solution().makeLargestSpecial('11011000')}'
assert Solution().makeLargestSpecial('10') == "10", \
    f'Expected: "10", Received: {Solution().makeLargestSpecial('10')}'
