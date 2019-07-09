class TreeNode:

    def __init__(self, value, link_obj):
        self.left = None
        self.right = None
        self.value = value
        self.link_obj = link_obj

    def insert(self, value, link_obj):
        # Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = TreeNode(value, link_obj)
                else:
                    self.left.insert(value, link_obj)
            elif value > self.value:
                if self.right is None:
                    self.right = TreeNode(value, link_obj)
                else:
                    self.right.insert(value, link_obj)
        else:
            self.value = value
            self.link_obj = link_obj

    def find_left_nearest_node(self, value):
        res_node = None
        current_node = self
        while current_node:
            if current_node.value < value:
                res_node = current_node
                current_node = current_node.right
            elif current_node.value > value:
                current_node = current_node.left
            else:
                return current_node

        return res_node
