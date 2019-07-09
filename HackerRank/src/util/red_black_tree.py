class RbNode:
    def __init__(self, k=0):
        self.key = k
        self.color = 0
        self.parent = None
        self.left = None
        self.right = None


class RbTree:
    def __init__(self):
        self.null = RbNode()
        self.root = self.null


def left_rotate(tree, node):
    y = node.right
    node.right = y.left
    if y.left != tree.null:
        y.left.parent = node
    y.parent = node.parent
    if node.parent == tree.null:
        tree.root = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.left = node
    node.parent = y


def right_rotate(tree, node):
    y = node.left
    node.left = y.right
    if y.right != tree.null:
        y.right.parent = node
    y.parent = node.parent
    if node.parent == tree.null:
        tree.root = y
    elif node == node.parent.left:
        node.parent.left = y
    else:
        node.parent.right = y
    y.right = node
    node.parent = y


def rb_insert(tree, entry):
    y = tree.null
    x = tree.root
    while x != tree.null:
        y = x
        if entry.key < x.key:
            x = x.left
        else:
            x = x.right
    entry.parent = y
    if y == tree.null:
        tree.root = entry
    elif entry.key < y.key:
        y.left = entry
    else:
        y.right = entry
    entry.left = tree.null
    entry.right = tree.null
    entry.color = 1
    rb_insert_fixup(tree, entry)


def rb_insert_fixup(tree, entry):
    while entry.parent.color == 1:
        if entry.parent == entry.parent.parent.left:
            y = entry.parent.parent.right
            if y.color == 1:
                entry.parent.color = 0
                y.color = 0
                entry.parent.parent.color = 1
                entry = entry.parent.parent
            else:
                if entry == entry.parent.right:
                    entry = entry.parent
                    left_rotate(tree, entry)
                entry.parent.color = 0
                entry.parent.parent.color = 1
                right_rotate(tree, entry.parent.parent)
        else:
            y = entry.parent.parent.left
            if y.color == 1:
                entry.parent.color = 0
                y.color = 0
                entry.parent.parent.color = 1
                entry = entry.parent.parent
            else:
                if entry == entry.parent.left:
                    entry = entry.parent
                    right_rotate(tree, entry)
                entry.parent.color = 0
                entry.parent.parent.color = 1
                left_rotate(tree, entry.parent.parent)
    tree.root.color = 0


def rb_transplant(tree, u, v):
    # replaces the subtree rooted at node u
    # with the subtree rooted at node v
    if u.parent == tree.null:
        tree.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    v.parent = u.parent


def tree_minimum(tree, node):
    while node.left != tree.null:
        node = node.left
    return node


def rb_delete(tree, z):
    y = z
    y_original_color = y.color
    if z.left == tree.null:
        x = z.right
        rb_transplant(tree, z, z.right)
    elif z.right == tree.null:
        x = z.left
        rb_transplant(tree, z, z.left)
    else:
        y = tree_minimum(tree, z.right)
        y_original_color = y.color
        x = y.right
        if y.parent == z:
            x.parent = y
        else:
            rb_transplant(tree, y, y.right)
            y.right = z.right
            y.right.parent = y
        rb_transplant(tree, z, y)
        y.left = z.left
        y.left.parent = y
        y.color = z.color
    if y_original_color == 0:
        rb_delete_fixup(tree, x)


def rb_delete_fixup(tree, x):
    while x != tree.root and x.color == 0:
        if x == x.parent.left:
            w = x.parent.right
            if w.color == 1:
                w.color = 0
                x.parent.color = 1
                left_rotate(tree, x.parent)
                w = x.parent.right
            if w.left.color == 0 and w.right.color == 0:
                w.color = 1
                x = x.parent
            else:
                if w.right.color == 0:
                    w.left.color = 0
                    w.color = 1
                    right_rotate(tree, w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = 0
                w.right.color = 0
                left_rotate(tree, x.parent)
                x = tree.root
        else:
            w = x.parent.left
            if w.color == 1:
                w.color = 0
                x.parent.color = 1
                right_rotate(tree, x.parent)
                w = x.parent.left
            if w.right.color == 0 and w.left.color == 0:
                w.color = 1
                x = x.parent
            else:
                if w.left.color == 0:
                    w.right.color = 0
                    w.color = 1
                    left_rotate(tree, w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = 0
                w.left.color = 0
                right_rotate(tree, x.parent)
                x = tree.root
    x.color = 0

