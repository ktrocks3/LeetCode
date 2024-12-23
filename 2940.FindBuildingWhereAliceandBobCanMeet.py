class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        mono_stack = []
        result = [-1 for _ in range(len(queries))]
        new_queries = [[] for _ in range(len(heights))]
        for i in range(len(queries)):
            a = queries[i][0]
            b = queries[i][1]
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        for i in range(len(heights) - 1, -1, -1):
            mono_stack_size = len(mono_stack)
            for a, b in new_queries[i]:
                position = self.search(a, mono_stack)
                if position < mono_stack_size and position >= 0:
                    result[b] = mono_stack[position][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))
        return result

    def search(self, height, mono_stack):
        left = 0
        right = len(mono_stack) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if mono_stack[mid][0] > height:
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans


assert Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7],
                                          [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]) == [2, 5, -1, 5, 2], \
    f'Expected: [2,5,-1,5,2], Received: {Solution().leftmostBuildingQueries([6, 4, 8, 5, 2, 7],
                                                                            [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]])}'
assert Solution().leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6],
                                          [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]) == [7, 6, -1, 4, 6], \
    f'Expected: [7,6,-1,4,6], Received: {Solution().leftmostBuildingQueries([5, 3, 8, 2, 6, 1, 4, 6],
                                                                            [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]])}'
