from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        hash = defaultdict(list)

        n = len(s)
        i = 0
        while i < n:
            temp = 1
            ch = s[i]
            while i < n - 1 and s[i] == s[i + 1]:
                temp += 1
                i += 1
            hash[ch].append(temp)
            i += 1

        maxi = -1
        for ch, lis in hash.items():
            lis.sort(reverse=True)
            if lis[0] >= 3:
                maxi = max(maxi, lis[0] - 2)
            if len(lis) >= 2:
                if lis[0] >= 2:
                    maxi = max(maxi, min(lis[0] - 1, lis[1]))
                if len(lis) >= 3:
                    maxi = max(maxi, lis[2])

        return maxi

        n = len(s)
        # freq=[[0]*(n+1) for _ in range(26)]
        freq = defaultdict(lambda: defaultdict(int))
        # freq[i][j] stores the count of special substrings of length j ending with the character at index i.

        pre = s[0];
        length = 1;
        ans = -1
        freq[s[0]][1] = 1  # ending with first letter, length j, count 1

        for i in range(1, n):
            cur = s[i]
            if cur == pre:
                length += 1
                freq[cur][length] += 1
            else:
                freq[cur][1] += 1
                pre = cur
                length = 1

        for k in freq.keys():  # for the char, k is char
            presum = 0
            for j in range(n, 0, -1):
                presum += freq[k][j]  # end with k, length is j, freq content is frequency
                if presum >= 3:
                    ans = max(ans, j)
                    break
        return ans


assert Solution().maximumLength('aaaa') == 2, \
  f'Expected: 2, Received: {Solution().maximumLength('aaaa')}'
assert Solution().maximumLength('abcdef') == -1, \
  f'Expected: -1, Received: {Solution().maximumLength('abcdef')}'
assert Solution().maximumLength('abcaba') == 1, \
  f'Expected: 1, Received: {Solution().maximumLength('abcaba')}'
Solution().maximumLength("acc")
Solution().maximumLength("aaa")
Solution().maximumLength("abcccccddddabcccccddddabcccccdddd")
Solution().maximumLength("jinhhhtttttttefffffjjjjjjjjjfffffjjjjjjjjjzvvvvvvg")
Solution().maximumLength("aaaaaaaaaaaaccccccccccccccccccccccccccaaaaaaaaaaaa")
Solution().maximumLength("aaaaaaaaaaaaaaaaaaaabbbbbbbbbbaaaaaaaaaaaaaaaaaaaa")
Solution().maximumLength("zzzzzzzzzzzzzzzzzfffffdddddddddiiiiiiiiiiiiiiiiiii")
Solution().maximumLength("zzzzzzzzzzzsssssssssssssssssqppppppppppppppnqmosat")
