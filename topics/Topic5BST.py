class Node:
    # key: int
    # value: int
    # left: Node
    # right: Node

    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # root: Node

    def __init__(self, root: Node = None):
        self.root = root
    
    # find 
    def find(self, node: Node, key: int):
        if(node is None):
            print("Key is not found.")
            return None
        if(node.key > key):
            # go left
            return self.find(node.left, key)
        elif(node.key < key):
            # go right
            return self.find(node.right, key)
        else:
            print("Found the key!")
            print(node.key)
            return node
        
    
    def put(self, node: Node, key: int, value: int):
        if(node is None):
            return  Node(key, value)
        if(node.key > key):
            node.left = self.put(node.left, key, value)
        elif(node.key < key):
            node.right = self.put(node.right, key, value)
        else:
            # when the key is equal then we update the value
            node.value = value
        return node


    # delete
    def delete(self, key: int):
        node = self.find(self.root, key)
        if(node is None):
            print("Cannot delete a node which isn't present.")
        # 0 child
        if(node.left is None and node.right is None):
            print("Deleting node")
            node = None
        # 1 child
        # 2 children
    
    # returns the minimum key present in the tree
    def min_key(self, node: Node):
        if(node.left is None):
            return node.key
        else:
            return self.min_key(node.left)

    # floor (recursive)

    # ceiling (recursive)

    # rank

    # traversal (in-order, pre-order, post-order)

    def in_order_traversal(self, node: Node):
        # left, middle, right
        # if left node is present keep going left
        if(node.left is not None):
            self.in_order_traversal(node.left)
        # when left node is not present (print the node)
        print("Key: "+str(node.key)+", Value: "+str(node.value))
        # if left & middle are done go right
        if(node.right is not None):
            self.in_order_traversal(node.right)

    def post_order_traversal(self, node: Node):
        # left, right, middle
        # if left node is present - keep going to the left
        if(node.left is not None):
            self.post_order_traversal(node.left)
        # no more left, now check if right node is present
        if(node.right is not None):
            self.post_order_traversal(node.right)
        # if left & right is not present - print the node
        print("Key: "+str(node.key)+", Value: "+str(node.value))
    
    def pre_order_traversal(self, node: Node):
        # middle, left, right
        # first print the current node
        print("Key: "+str(node.key)+", Value: "+str(node.value))
        # if left node is present go to the left node
        if(node.left is not None):
            self.pre_order_traversal(node.left)
        if(node.right is not None):
            self.pre_order_traversal(node.right)

if __name__ == '__main__':
    node1 = Node(10, 1)
    # node2 = Node('A', 5)
    # node3 = Node('C', 15)
    bst = BinarySearchTree(node1)
    bst.put(bst.root, 5, 5)
    bst.put(bst.root, 14, 15)
    bst.put(bst.root, 7, 1)
    bst.put(bst.root, 12, 1)
    bst.put(bst.root, 18, 1)
    bst.put(bst.root, 15, 1)

    # printing Nodes
    # print(bst.root.key)
    # print(bst.root.value)
    # print(bst.root.right.key)
    # print(bst.root.right.value)
    # print(bst.root.left.key)
    # print(bst.root.left.value)
    
    # in order traversal
    print("In-order traversal:")
    bst.in_order_traversal(bst.root)
    print()

    # bst.put(bst.root, 'D', 0)
    print("In-order traversal:")
    bst.in_order_traversal(bst.root)

    print()
    print("Pre-order traversal:")
    bst.pre_order_traversal(bst.root)
    
    print()
    print("Post-order traversal:")
    bst.post_order_traversal(bst.root)

    # find an element
    print(bst.find(bst.root, 15))
    print(bst.find(bst.root, 20))
    print(bst.find(bst.root, 14))
    print(bst.find(bst.root, 12))

    # deleting an element
    bst.delete(15)
    bst.in_order_traversal(bst.root)