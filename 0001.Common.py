class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertArr(arr) -> TreeNode:
    if not arr:
        return None

    def build_tree(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        root = TreeNode(arr[mid])
        root.left = build_tree(start, mid - 1)
        root.right = build_tree(mid + 1, end)
        return root

    return build_tree(0, len(arr) - 1)


def convertTree(root: TreeNode) -> list:
    def in_order_traversal(node):
        if not node:
            return []
        # Traverse left subtree, then root, then right subtree
        return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

    return in_order_traversal(root)


