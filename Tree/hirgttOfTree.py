

# https://medium.com/techie-delight/binary-tree-interview-questions-and-practice-problems-439df7e5ea1f


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Recursive function to calculate height of given binary Tree
def treeHeight(root):
    # Base case: empty Tree has height 0
    if root is None:
        return 0
    else:
        leftHeight = treeHeight(root.left)
        rightHeight = treeHeight(root.right)

    # recur for left and right subtree and consider maximum depth
    return 1 + max(leftHeight, rightHeight)


if __name__ == '__main__':
    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)

    print("The height of the binary Tree is", treeHeight(root))
