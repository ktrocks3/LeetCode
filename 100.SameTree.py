from typing import Optional

from common import TreeNode, convertArr


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val



p, q = [1, 2, 3], [1, 2, 3]
assert Solution().isSameTree(convertArr(p), convertArr(q)) == True
p, q = [1, 2], [1, None, 2]
assert Solution().isSameTree(convertArr(p), convertArr(q)) == False
p, q = [1, 2, 1], [1, 1, 2]
assert Solution().isSameTree(convertArr(p), convertArr(q)) == False
