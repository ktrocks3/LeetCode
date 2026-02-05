from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        spaces = set(spaces)
        for i, c in enumerate(s):
            if i in spaces:
                res.append(' ')
            res.append(c)
        return ''.join(res)


assert Solution().addSpaces('LeetcodeHelpsMeLearn', [8, 13, 15]) == "Leetcode Helps Me Learn", \
    f'Expected: "Leetcode Helps Me Learn", Received: {Solution().addSpaces('LeetcodeHelpsMeLearn', [8, 13, 15])}'
assert Solution().addSpaces('icodeinpython', [1, 5, 7, 9]) == "i code in py thon", \
    f'Expected: "i code in py thon", Received: {Solution().addSpaces('icodeinpython', [1, 5, 7, 9])}'
assert Solution().addSpaces('spacing', [0, 1, 2, 3, 4, 5, 6]) == " s p a c i n g", \
    f'Expected: " s p a c i n g", Received: {Solution().addSpaces('spacing', [0, 1, 2, 3, 4, 5, 6])}'
Solution().addSpaces("LeetcodeHelpsMeLearn", [8, 13, 15])
Solution().addSpaces("icodeincpp", [1, 5, 7, 9])
Solution().addSpaces("spacing", [0, 1, 2, 3, 4, 5, 6])
Solution().addSpaces("AllEyesOnHindu", [7])
Solution().addSpaces("MakeIndiaGreatAgain", [1, 7, 8, 9])
Solution().addSpaces("DelhiMeiBJP", [8, 9])
Solution().addSpaces("HinduMeansIndian", [9, 11])
Solution().addSpaces("jaimatadi", [7, 8])
