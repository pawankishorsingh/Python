class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    root = Node(None)
    def pre_order_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            print(root.data, end=" ")
            self.in_order_traversal(root.right)
    def post_order_traversal(self, root):
        if root:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.data, end=" ")

if __name__ == '__main__':
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    print("Pre order:", end="")
    tree.pre_order_traversal(tree.root)
    print("\nIn order:", end="")
    tree.in_order_traversal(tree.root)
    print("\nPost order:", end="")
    tree.post_order_traversal(tree.root)




