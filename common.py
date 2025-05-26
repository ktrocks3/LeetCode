class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

    def __str__(self):
        left_val  = self.left.val  if self.left  else None
        right_val = self.right.val if self.right else None
        return f"TreeNode(val={self.val}, left={left_val}, right={right_val})"

def convertArr(arr) -> TreeNode:
    if not arr:
        return None

    # 1) Build a parallel list of nodes, but leave None entries as None
    nodes = [None if v is None else TreeNode(v) for v in arr]

    # 2) Now wire up children. We’ll walk through `nodes` with an index.
    child_idx = 1
    for parent in nodes:
        if parent is None:
            continue  # skip holes in the tree

        # assign left child
        if child_idx < len(nodes):
            parent.left = nodes[child_idx]
            child_idx += 1

        # assign right child
        if child_idx < len(nodes):
            parent.right = nodes[child_idx]
            child_idx += 1

    # the root is the first element
    return nodes[0]



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
