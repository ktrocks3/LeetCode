class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        # Pad with 0s
        if len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        elif len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        res, carry = [], False
        a, b = a[::-1], b[::-1]
        for i in range(len(a)):
            if a[i] == '1' and b[i] == '1':
                if carry:
                    res.append('1')
                else:
                    res.append('0')
                    carry = True
            elif a[i] == '0' and b[i] == '1' or a[i] == '1' and b[i] == '0':
                if carry:
                    res.append('0')
                else:
                    res.append('1')
                    carry = False

            else:
                if carry:
                    res.append('1')
                    carry = False
                else:
                    res.append('0')
        if carry:
            res.append('1')

        res = ''.join(res[::-1])
        return res

    def addBinary2(self, a: str, b: str) -> str:
        res, carry = [], 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Sum of two bits and carry
            total = bit_a + bit_b + carry
            res.append(str(total % 2))  # Append current bit (0 or 1)
            carry = total // 2  # Update carry (0 or 1)

            i, j = i - 1, j - 1

        return ''.join(reversed(res))

    def addBinary3(self, a: str, b: str) -> str:
        a_int = int(a, 2)
        b_int = int(b, 2)

        sum_int = a_int + b_int

        return bin(sum_int)[2:]


assert Solution().addBinary1("11", "1") == "100", \
    f"Expected: 100, Actual: {Solution().addBinary1("11", "1")}"
assert Solution().addBinary2("1010", "1011") == "10101", \
    f"Expected: 10101, Actual: {Solution().addBinary2("1010", "1011")}"
assert Solution().addBinary3("1111", "1111") == "11110", \
    f"Expected: 11110, Actual: {Solution().addBinary3("1111", "1111")}"
