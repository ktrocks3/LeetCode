class Solution:
    def minPartitions(self, n: str) -> int:
        for d in "987654321":
            if d in n:
                return int(d)


assert Solution().minPartitions('32') == 3, \
  f'Expected: 3, Received: {Solution().minPartitions('32')}'
assert Solution().minPartitions('82734') == 8, \
  f'Expected: 8, Received: {Solution().minPartitions('82734')}'
assert Solution().minPartitions('27346209830709182346') == 9, \
  f'Expected: 9, Received: {Solution().minPartitions('27346209830709182346')}'