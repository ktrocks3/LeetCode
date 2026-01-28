from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0 for _ in range(n)]
        for l in logs:
            proc_id, proc_type, time = l.split(':')
            time = int(time)
            if proc_type == 'start':
                if stack:
                    x, y, z = stack.pop()
                    stack.append((x, y, time - y + z))
                stack.append((proc_id, time, 0))
            if proc_type == 'end':
                x, y, z = stack.pop()
                result[int(x)] += (time - y + z + 1)
                if stack:
                    x, y, z = stack.pop()
                    stack.append((x, time + 1, z))
        return result


assert Solution().exclusiveTime(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6']) == [3, 4], \
    f'Expected: [3,4], Received: {Solution().exclusiveTime(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6'])}'
assert Solution().exclusiveTime(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']) == [8], \
    f'Expected: [8], Received: {Solution().exclusiveTime(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7'])}'
assert Solution().exclusiveTime(2, ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']) == [7, 1], \
    f'Expected: [7,1], Received: {Solution().exclusiveTime(2, ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7'])}'
