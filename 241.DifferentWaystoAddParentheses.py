from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> set[int]:
        res = set()
        # Iterate through the string looking for operators
        for i, c in enumerate(expression):
            if c in {'+', '-', '*'}:
                # Recursively solve for left and right sides
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i + 1:])

                # Combine the results based on the current operator
                for left in left_results:
                    for right in right_results:
                        if c == '+':
                            res.add(left + right)
                        elif c == '-':
                            res.add(left - right)
                        elif c == '*':
                            res.add(left * right)

        # If there are no operators, return the number as the only result
        if not res:
            res.add(int(expression))
        return res


# Test cases
assert set(Solution().diffWaysToCompute("2-1-1")) == {0, 2}
assert set(Solution().diffWaysToCompute("2*3-4*5")) == {-34, -14, -10, 10}
