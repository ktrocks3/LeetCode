class Solution:
    def maxKDivisibleComponents(n, edges, values, k):
        from collections import defaultdict
        import sys
        sys.setrecursionlimit(10 ** 6)

        # Create adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(node, parent):
            # Cumulative sum of the current subtree
            total_sum = values[node]
            # Number of valid splits in this subtree
            splits = 0

            # Traverse children
            for neighbor in tree[node]:
                if neighbor != parent:
                    child_sum, child_splits = dfs(neighbor, node)
                    # Add child's splits to the current splits
                    splits += child_splits

                    # If the child's cumulative sum is divisible by k, split here
                    if child_sum % k == 0:
                        splits += 1
                    else:
                        # Add child's sum to the current node's total_sum
                        total_sum += child_sum

            return total_sum, splits

        # Start DFS from node 0
        _, total_splits = dfs(0, -1)

        # The total components = total splits + 1
        return total_splits + 1
