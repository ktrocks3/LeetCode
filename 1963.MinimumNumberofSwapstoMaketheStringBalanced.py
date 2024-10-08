class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_imbalance = 0

        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1

            # Track the maximum imbalance
            max_imbalance = min(max_imbalance, balance)

        # The number of swaps needed is half of the max imbalance (rounded up)
        return (-max_imbalance + 1) // 2


assert Solution().minSwaps("][][") == 1
assert Solution().minSwaps("]]][[[") == 2
assert Solution().minSwaps("[]") == 0
