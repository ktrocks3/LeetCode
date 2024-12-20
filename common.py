class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convertArr(arr) -> TreeNode:
    if not arr:
        return None

    root = TreeNode(arr[0])  # First element is the root
    queue = [root]
    i = 1

    # Use a queue to assign left and right children in a level-order manner
    while i < len(arr):
        current = queue.pop(0)
        if i < len(arr):
            current.left = TreeNode(arr[i])
            queue.append(current.left)
            i += 1
        if i < len(arr):
            current.right = TreeNode(arr[i])
            queue.append(current.right)
            i += 1

    return root



def convertTree(root: TreeNode) -> list:
    if not root:
        return []

    result = []
    queue = [root]  # Use a queue for level-order traversal

    while queue:
        current = queue.pop(0)  # Get the first node in the queue
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result



