from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def find_diameter_and_radius(edges):
            # Helper to find farthest node and distance from a given start node
            def bfs(start):
                visited = set()
                queue = deque([(start, 0)])
                farthest_node, max_distance = start, 0
                while queue:
                    node, dist = queue.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    if dist > max_distance:
                        max_distance = dist
                        farthest_node = node
                    for neighbor in edges[node]:
                        if neighbor not in visited:
                            queue.append((neighbor, dist + 1))
                return farthest_node, max_distance

            # Step 1: Find one end of the diameter
            any_node = next(iter(edges))  # Start from any node
            farthest_node, _ = bfs(any_node)

            # Step 2: Find the actual diameter
            other_end, diameter = bfs(farthest_node)

            # Step 3: Calculate the radius
            radius = (diameter + 1) // 2  # Radius is half of diameter (rounded up)
            return diameter, radius

        # Build adjacency lists for both trees
        def build_adjacency_list(edges):
            adj_list = defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
            return adj_list

        tree1 = build_adjacency_list(edges1)
        tree2 = build_adjacency_list(edges2)

        # Compute diameter and radius for both trees
        diameter1, radius1 = find_diameter_and_radius(tree1) if len(tree1) > 0 else (0, 0)
        diameter2, radius2 = find_diameter_and_radius(tree2) if len(tree2) > 0 else (0, 0)

        # The minimum diameter after merging
        return max(diameter1, diameter2, radius1 + radius2 + 1)


# Test cases
assert Solution().minimumDiameterAfterMerge([[0, 1], [0, 2], [0, 3]], [[0, 1]]) == 3, \
    f"Test case 1 failed"
assert Solution().minimumDiameterAfterMerge(
    [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]],
    [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
) == 5, f"Test case 2 failed"
assert Solution().minimumDiameterAfterMerge(
    [], []
) == 0, f"Test case 2 failed"
assert Solution().minimumDiameterAfterMerge(
    [[0, 1], [2, 0], [3, 2], [3, 6], [8, 7], [4, 8], [5, 4], [3, 5], [3, 9]],
    [[0, 1], [0, 2], [0, 3]]
) == 7, f"Test case 3 failed"

