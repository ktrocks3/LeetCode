from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        oddSum = []
        evenSum = []
        n = len(nums)
        for i, num in enumerate(nums):
            if i % 2 == 0:
                if i == 0:
                    evenSum.append(num)
                    oddSum.append(0)
                else:
                    evenSum.append(num + evenSum[-1])
                    oddSum.append(oddSum[-1])
            else:
                oddSum.append(num + oddSum[-1])
                evenSum.append(evenSum[-1])
        total = 0
        for i in range(n):
            leftOdd = oddSum[i - 1] if i > 0 else 0
            leftEven = evenSum[i - 1] if i > 0 else 0

            tempOddSum = leftOdd + (evenSum[n - 1] - evenSum[i])
            tempEvenSum = leftEven + (oddSum[n - 1] - oddSum[i])

            if tempOddSum == tempEvenSum:
                total += 1
        return total


# Solution().waysToMakeFair([6, 1, 7, 4, 1])
assert Solution().waysToMakeFair([2, 1, 6, 4]) == 1, \
    f'Expected: 1, Received: {Solution().waysToMakeFair([2, 1, 6, 4])}'
assert Solution().waysToMakeFair([1, 1, 1]) == 3, \
    f'Expected: 3, Received: {Solution().waysToMakeFair([1, 1, 1])}'
assert Solution().waysToMakeFair([1, 2, 3]) == 0, \
    f'Expected: 0, Received: {Solution().waysToMakeFair([1, 2, 3])}'
