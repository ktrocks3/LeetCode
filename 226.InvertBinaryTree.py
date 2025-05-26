from common import TreeNode, convertArr, convertTree
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.right = r
        root.left = l
        return root

Input = [4,2,7,1,3,6,9]
Output= [4,7,2,9,6,3,1]
assert convertTree(Solution().invertTree(convertArr(Input))) == Output, convertTree(Solution().invertTree(convertArr(Input)))

Input = [2,1,3]
Output= [2,3,1]
assert convertTree(Solution().invertTree(convertArr(Input))) == Output

Input = []
Output= []
assert convertTree(Solution().invertTree(convertArr(Input))) == Output
