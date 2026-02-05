class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        locs = []
        order = []
        for i, x in enumerate(s):
            if x in vowels:
                locs.append(i)
                order.append(x)
        order.sort(key=lambda x: ord(x), reverse=True)
        s = list(s)
        for loc in locs:
            s[loc] = order.pop()
        return ''.join(s)


assert Solution().sortVowels('lEetcOde') == "lEOtcede", \
  f'Expected: "lEOtcede", Received: {Solution().sortVowels('lEetcOde')}'
assert Solution().sortVowels('lYmpH') == "lYmpH", \
  f'Expected: "lYmpH", Received: {Solution().sortVowels('lYmpH')}'