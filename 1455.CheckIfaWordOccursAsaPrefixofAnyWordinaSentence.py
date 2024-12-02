class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split()):
            if word[:len(searchWord)] == searchWord:
                return i + 1
        return -1


assert Solution().isPrefixOfWord('i love eating burger', 'burg') == 4, \
    f'Expected: 4, Received: {Solution().isPrefixOfWord('i love eating burger', 'burg')}'
assert Solution().isPrefixOfWord('this problem is an easy problem', 'pro') == 2, \
    f'Expected: 2, Received: {Solution().isPrefixOfWord('this problem is an easy problem', 'pro')}'
assert Solution().isPrefixOfWord('i am tired', 'you') == -1, \
    f'Expected: -1, Received: {Solution().isPrefixOfWord('i am tired', 'you')}'
Solution().isPrefixOfWord("i love eating bunburger burger", "burg")
Solution().isPrefixOfWord("hellohello hellohellohello", "ello")
Solution().isPrefixOfWord("i love eating broadburgers", "burg")
Solution().isPrefixOfWord("love i love eating bunburger burger", "i")
Solution().isPrefixOfWord("helloh hellohe", "hellohe")
Solution().isPrefixOfWord("winstontang love they i pillow jonathan you winstontang pillow dream you duck", "p")
Solution().isPrefixOfWord("love", "lov")
Solution().isPrefixOfWord("hello from the other side", "they")
