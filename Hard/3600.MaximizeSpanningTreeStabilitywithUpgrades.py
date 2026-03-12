from typing import List


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        size = [1] * n

        def find_set(v):
            if parent[v] == v:
                return v
            parent[v] = find_set(parent[v])
            return parent[v]

        def union_sets(a, b):
            a = find_set(a)
            b = find_set(b)

            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                return True
            else:
                return False

        def same_set(a, b):
            a = find_set(a)
            b = find_set(b)
            return a != b

        components = n
        min_stability = float("inf")

        optional = []
        for index, edge in enumerate(edges):
            if edge[3]:
                # edge must be included
                if union_sets(edge[0], edge[1]):
                    components -= 1
                    min_stability = min(min_stability, edge[2])
                else:
                    # the edges that have to be included form a cycle
                    return -1
            else:
                optional.append(index)

        if components == 1:
            # no more edges can be added
            return min_stability

        # sort optional edges by stability
        optional.sort(key=lambda x: edges[x][2], reverse=True)

        stabilities = []
        for index in optional:
            edge = edges[index]
            if union_sets(edge[0], edge[1]):
                # edge was added
                components -= 1
                stabilities.append(edge[2])

                if components == 1:
                    break

        if components > 1:
            # cannot connect tree
            return -1

        # use upgrades on edges with smallest stability
        for i in range(1, min(len(stabilities), k) + 1):
            stabilities[-i] *= 2

        return min(min(stabilities), min_stability)


assert Solution().maxStability(3, [[0, 1, 2, 1], [1, 2, 3, 0]], 1) == 2, \
  f'Expected: 2, Received: {Solution().maxStability(3, [[0, 1, 2, 1], [1, 2, 3, 0]], 1)}'
assert Solution().maxStability(3, [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], 2) == 6, \
  f'Expected: 6, Received: {Solution().maxStability(3, [[0, 1, 4, 0], [1, 2, 3, 0], [0, 2, 1, 0]], 2)}'
assert Solution().maxStability(3, [[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], 0) == -1, \
  f'Expected: -1, Received: {Solution().maxStability(3, [[0, 1, 1, 1], [1, 2, 1, 1], [2, 0, 1, 1]], 0)}'