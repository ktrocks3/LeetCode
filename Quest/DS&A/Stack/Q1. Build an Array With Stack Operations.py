from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        idx = 0
        m = len(target)

        for num in range(1, min(n, target[-1]) + 1):
            res.append("Push")
            if num == target[idx]:
                idx += 1
                if idx == m:
                    break
            else:
                res.append("Pop")

        return res




assert Solution().buildArray([1, 3], 3) == ["Push","Push","Pop","Push"], \
  f'Expected: ["Push","Push","Pop","Push"], Received: {Solution().buildArray([1, 3], 3)}'
assert Solution().buildArray([1, 2, 3], 3) == ["Push","Push","Push"], \
  f'Expected: ["Push","Push","Push"], Received: {Solution().buildArray([1, 2, 3], 3)}'
assert Solution().buildArray([1, 2], 4) == ["Push","Push"], \
  f'Expected: ["Push","Push"], Received: {Solution().buildArray([1, 2], 4)}'