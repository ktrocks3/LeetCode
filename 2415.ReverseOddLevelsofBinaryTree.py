from typing import Optional
from common import TreeNode, convertTree, convertArr


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        # Queue for level-order traversal
        queue = deque([root])
        level = 0  # Start at root level

        while queue:
            # Collect all nodes at the current level
            level_size = len(queue)
            current_level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                current_level_nodes.append(node)

            # Reverse values at odd levels
            if level % 2 == 1:
                values = [node.val for node in current_level_nodes]
                reversed_values = values[::-1]
                for i, node in enumerate(current_level_nodes):
                    node.val = reversed_values[i]

            # Move to the next level
            level += 1

        return root


assert convertTree(Solution().reverseOddLevels(convertArr([2, 3, 5, 8, 13, 21, 34]))) == [2, 5, 3, 8, 13, 21, 34], \
    f'Expected: [2,5,3,8,13,21,34], Received: {convertTree(Solution().reverseOddLevels(convertArr([2, 3, 5, 8, 13, 21, 34])))}'
assert convertTree(Solution().reverseOddLevels(convertArr([7, 13, 11]))) == [7, 11, 13], \
    f'Expected: [7,11,13], Received: {convertTree(Solution().reverseOddLevels(convertArr([7, 13, 11])))}'
assert convertTree(Solution().reverseOddLevels(convertArr([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]))) == [
    0, 2, 1, 0, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1, 1], \
    (f'Expected: [0,2,1,0,0,0,0,2,2,2,2,1,1,1,1], Received: '
     f'{convertTree(Solution().reverseOddLevels(convertArr([0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2])))}')
