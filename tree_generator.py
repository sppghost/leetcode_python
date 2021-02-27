class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeGenerator:

    def __init__(self, s: str):
        s = s[1:-1]
        self.nodes = list(map(lambda x: int(x) if x.isdigit() else None, s.split(',')))
        self.pre_res = []
        self.in_res = []
        self.post_res = []

    def generation(self) -> TreeNode:
        if len(self.nodes) == 0:
            return None
        return self.dfs(0)

    def dfs(self, i):
        if i >= len(self.nodes) or self.nodes[i] is None:
            return None
        root = TreeNode(self.nodes[i])
        root.left = self.dfs(2 * i + 1)
        root.right = self.dfs(2 * i + 2)
        return root

    def preorder(self, root):
        if root is None:
            return
        self.pre_res.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.in_res.append(root.val)
        self.inorder(root.right)

    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.post_res.append(root.val)


if __name__ == '__main__':
    tree = '[3,9,20,null,null,15,7]'
    tg = TreeGenerator(tree)
    root = tg.generation()
    tg.preorder(root)
    tg.inorder(root)
    tg.postorder(root)
    print(tg.pre_res)
    print(tg.in_res)
    print(tg.post_res)
