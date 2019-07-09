from util.timer import timer_func
from util.tree import TreeNode


class Node:
    def __init__(self):
        self.index = 0
        self.data_val = 0
        self.next_values = 0
        self.next_node = None
        self.prev_node = None

    def __str__(self) -> str:
        return f"Index {self.index} - Value {self.data_val} - Next {self.next_values}"


class SLinkedList:
    def __init__(self):
        self.head_node = None
        self.bst = None

    def _init_head(self, start, stop, value):
        start_node = Node()
        start_node.index = start
        start_node.data_val = value
        start_node.next_values = value

        self.bst = TreeNode(start_node.index, start_node)
        self.head_node = start_node

        end_node = Node()
        end_node.index = stop
        end_node.data_val = value
        end_node.prev_node = self.head_node

        self.bst.insert(end_node.index, end_node)
        self.head_node.next_node = end_node

    def max_value(self):
        max_data = 0
        current_node = self.head_node
        while current_node is not None:
            if current_node.data_val > max_data:
                max_data = current_node.data_val
            current_node = current_node.next_node
        return max_data

    @timer_func
    def _find_left_node(self, index):
        if index < self.head_node.index:
            return None
        """
        current_node = self.head_node
        prev_node = None
        while current_node is not None:
            if current_node.index <= index:
                prev_node = current_node
                current_node = current_node.next_node
                continue

            return current_node.prev_node

        return prev_node
        """
        tree_node = self.bst.find_left_nearest_node(index)
        return tree_node if not tree_node else tree_node.link_obj

    def _insert_node(self, left, index) -> Node:
        new_node = Node()
        new_node.index = index
        new_node.prev_node = left if left else None
        new_node.next_node = left.next_node if left else self.head_node

        self.bst.insert(new_node.index, new_node)

        if not left:
            self.head_node.prev_node = new_node
            self.head_node = new_node
            return new_node

        if left.next_node:
            left.next_node.prev_node = new_node
        left.next_node = new_node

        return new_node

    def _insert_interval(self, start, stop, value):
        left_node_a = self._find_left_node(start)
        if left_node_a and left_node_a.index == start:
            new_start_node = left_node_a
        else:
            new_start_node = self._insert_node(left_node_a, start)

        if left_node_a and left_node_a.index != start:
            new_start_node.data_val = value + left_node_a.next_values
            new_start_node.next_values = value + left_node_a.next_values
        else:
            new_start_node.data_val += value
            new_start_node.next_values += value

        left_node_b = self._find_left_node(stop)
        if left_node_b and left_node_b.index == stop:
            new_end_node = left_node_b
        else:
            new_end_node = self._insert_node(left_node_b, stop)

        update_node = new_start_node.next_node
        self._update_interval(new_end_node, update_node, value)

        if left_node_b.index != stop:
            new_end_node.data_val = left_node_b.next_values
            new_end_node.next_values = left_node_b.next_values - value
        else:
            new_end_node.data_val += value

    @staticmethod
    @timer_func
    def _update_interval(new_end_node, update_node, value):
        while update_node and update_node != new_end_node:
            update_node.data_val += value
            update_node.next_values += value
            update_node = update_node.next_node

    def _insert_point(self, index, value):
        left_node_a = self._find_left_node(index)
        if left_node_a and left_node_a.index == index:
            new_start_node = left_node_a
        else:
            new_start_node = self._insert_node(left_node_a, index)

        if left_node_a and left_node_a.index != index:
            new_start_node.data_val = value + left_node_a.next_values
            new_start_node.next_values = left_node_a.next_values
        else:
            new_start_node.data_val += value

    def add_interval(self, start, stop, value):
        if not self.head_node:
            self._init_head(start, stop, value)
            return

        if start == stop:
            self._insert_point(start, value)
        else:
            self._insert_interval(start, stop, value)

    def print(self):
        print_node = self.head_node
        print('------------------------------------')
        while print_node is not None:
            print(print_node)
            print_node = print_node.next_node
        print('Max value: ', self.max_value())
