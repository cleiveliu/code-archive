from queue import Queue

# binary tree
class BNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


# preorder traversal
def preorder_recv(node):
    ret = []
    if not node:
        return ret
    ret.append(node.value)
    ret.extend(preorder_recv(node.left))
    ret.extend(preorder_recv(node.right))

    return ret

# None recv
# some kind of None well


def preorder(node):
    if not node:
        return []

    ret = []
    left, right = [node], []
    while left or right:
        if left:
            node = left.pop(0)
        else:
            node = right.pop().right
        ret.append(node.value)
        if node.left:
            left.append(node.left)
        if node.right:
            right.append(node)
    return ret


def preorder2(node):
    if not node:
        return []
    stack = [node]
    ret = []
    while stack:
        node = stack.pop()
        ret.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return ret


root = BNode(1)
root.left = BNode(2)
root.right = BNode(3)
root.left.left = BNode(4)
root.left.right = BNode(5)
root.right.left = BNode(6)
root.right.right = BNode(7)

print(preorder(root))

print(preorder2(root))
print(preorder_recv(root))


# inorder
def inorder_recv(root):
    ret = []
    if not root:
        return ret
    ret.extend(inorder_recv(root.left))
    ret.append(root.value)
    ret.extend(inorder_recv(root.right))

    return ret


def inorder(root):
    ret = []
    if not root:
        return ret
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            ret.append(node.value)
            node = node.right
    return ret


print(inorder(root))
print(inorder_recv(root))


# post_order

def post_order_recv(root):
    ret = []
    if not root:
        return ret
    ret.extend(post_order_recv(root.left))
    ret.extend(post_order_recv(root.right))
    ret.append(root.value)

    return ret


def post_order(root):
    ret = []
    if not root:
        return ret
    stack = []
    node = root
    visited = set()
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                ret.append(node.value)
                node = None
    return ret


print(post_order(root))
print(post_order_recv(root))


# level order


def level_order(root):
    ret = []
    if not root:
        return ret
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        ret.append(node.value)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)
    return ret


print(level_order(root))


# find max in a binary tree

def find_max_recv(root):
    ret = float('-inf')
    if not root:
        return ret
    ret = max(ret, root.value)
    left_max = find_max_recv(root.left)
    right_max = find_max_recv(root.right)

    return max(ret, left_max, right_max)


def find_max(root):
    ret = float('-inf')
    if not root:
        return ret
    q = Queue()
    q.put(root)
    while not q.empty():
        node = q.get()
        ret = max(ret, node.value)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return ret


print(find_max_recv(root))
print(find_max(root))
