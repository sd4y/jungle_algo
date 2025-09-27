import sys

tree = {}
root = int(sys.stdin.readline())
tree[root] = [None, None]
try:
    while True:
        parent = root

        node = int(sys.stdin.readline())

        if not node:
            break

        tree[node] = [None, None]

        while True:
            if node < parent :
                if tree[parent][0] is None:
                    tree[parent][0] = node
                    break
                else:
                    parent = tree[parent][0]
            else:
                if tree[parent][1] is None:
                    tree[parent][1] = node
                    break
                else:
                    parent = tree[parent][1]
except:
    pass

def postorder(_root):
    if _root is not None:
        postorder(tree[_root][0])
        postorder(tree[_root][1])
        print(_root)

postorder(root)

