# Definition for a binary tree node.
from typing import Optional, List
from common import TreeNode, convertArr


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


assert Solution().inorderTraversal(None) == [], Solution().inorderTraversal(None)
assert Solution().inorderTraversal(convertArr([1])) == [1], Solution().inorderTraversal(convertArr([1]))
assert Solution().inorderTraversal(convertArr([1, None, 2, 3])) == [1, 3, 2], (
    Solution().inorderTraversal(convertArr([1, None, 2, 3])))
a = [1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]
r = [4, 2, 6, 5, 7, 1, 3, 9, 8]
assert (Solution().inorderTraversal(convertArr(a)) == r), (Solution().inorderTraversal(convertArr(a)))
