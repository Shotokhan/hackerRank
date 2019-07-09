class Interval:
    def __init__(self, low=0, high=0):
        self.low = low
        self.high = high


class IntNode:
    def __init__(self, low=0, high=0, value=0):
        self.int = Interval(low, high)
        self.max = high
        self.color = 0
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def __str__(self) -> str:
        color = "Black" if self.color == 0 else "Red"
        """
        return f"Low : {self.int.low} High: {self.int.high} " \
            f"Max: {self.max} Value: {self.value} Color: {color}"
        """
        return f"{self.int.low} {self.int.high} {color}"

class IntTree:
    def __init__(self):
        self.null = IntNode()
        self.root = self.null
        self.maximum = 0

    def print(self, node=None, offset=0):
        if not node:
            node = self.root
        if node != self.null:
            self.print(node.left, offset + 4)
            print(offset*" " + f"{node}")
            self.print(node.right, offset + 4)
        else:
            print(offset*" " + "Null")

    def add_node(self, low, high, value):
        # add a node in such a way to have
        # all disjointed intervals
        x = interval_search(self, Interval(low, high))
        node = IntNode(low, high, value)
        if x != self.null:
            v = value + x.value
            xLow = x.int.low
            xHigh = x.int.high
            xValue = x.value
            if low <= x.int.low:
                if low < x.int.low:
                    self.add_node(low, x.int.low - 1, value)
                if high >= x.int.high:
                    if high > x.int.high:
                        self.add_node(x.int.high + 1, high, value)
                    x.value = v
                else:
                    rb_delete(self, x)
                    rb_insert(self, IntNode(xLow, high, v))
                    rb_insert(self, IntNode(high + 1, xHigh, xValue))
            elif high >= x.int.high:
                if high > x.int.high:
                    self.add_node(x.int.high + 1, high, value)
                rb_delete(self, x)
                rb_insert(self, IntNode(xLow, low - 1, xValue))
                rb_insert(self, IntNode(low, xHigh, v))
            else:
                rb_delete(self, x)
                rb_insert(self, IntNode(xLow, low - 1, xValue))
                rb_insert(self, IntNode(low, high, v))
                rb_insert(self, IntNode(high + 1, xHigh, xValue))

            if v > self.maximum:
                self.maximum = v
        else:
            rb_insert(self, node)
            if value > self.maximum:
                self.maximum = value


def upd_max(tree, node):
    if node.left != tree.null and node.left:
        if node.right != tree.null and node.right:
            M = max(node.left.max, node.right.max)
            node.max = max(M, node.int.high)
        else:
            node.max = max(node.left.max, node.int.high)
    elif node.right != tree.null and node.right:
        node.max = max(node.right.max, node.int.high)
    else:
        node.max = node.int.high


def overlap(interval1, interval2):
    if interval1.high < interval2.low:
        return 0
    elif interval1.low > interval2.high:
        return 0
    else:
        return 1


def interval_search(tree, interval):
    x = tree.root
    while x != tree.null and not overlap(x.int, interval):
        if x.left != tree.null and x.left.max >= interval.low:
            x = x.left
        else:
            x = x.right
    return x


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
    upd_max(tree, node)
    upd_max(tree, y)


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
    upd_max(tree, node)
    upd_max(tree, node)


def rb_insert(tree, entry):
    y = tree.null
    x = tree.root
    while x != tree.null:
        y = x
        if y.max < entry.int.high:
            y.max = entry.int.high
        if entry.int.low < x.int.low:
            x = x.left
        else:
            x = x.right
    entry.parent = y
    if y == tree.null:
        tree.root = entry
    elif entry.int.low < y.int.low:
        y.left = entry
    else:
        y.right = entry
    entry.right = tree.null
    entry.left = tree.null
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
    upd_max(tree, v.parent)


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
