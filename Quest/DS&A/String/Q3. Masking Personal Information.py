class Solution:
    def maskPII(self, s: str) -> str:
        isEmail = '@' in s
        if isEmail:
            s = s.lower()
            name, domain = s.split('@')
            return name[0] + '*' * 5 + name[-1] + '@' + domain
        else:
            for sep in {'+', '-', '(', ')', ' '}:
                s = s.replace(sep, '')
            code = s[:len(s) - 10]
            num = s[-4:]
            if len(code) == 0:
                return '***-***-' + num
            else:
                return f'+{"*" * len(code)}-***-***-XXXX' + num


assert Solution().maskPII('LeetCode@LeetCode.com') == "l*****e@leetcode.com", \
    f'Expected: "l*****e@leetcode.com", Received: {Solution().maskPII('LeetCode@LeetCode.com')}'
assert Solution().maskPII('AB@qq.com') == "a*****b@qq.com", \
    f'Expected: "a*****b@qq.com", Received: {Solution().maskPII('AB@qq.com')}'
assert Solution().maskPII('1(234)567-890') == "***-***-7890", \
    f'Expected: "***-***-7890", Received: {Solution().maskPII('1(234)567-890')}'
