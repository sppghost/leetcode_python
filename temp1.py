# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        temp1 = [root]
        if (root.val & 1) == 0:
            return False
        temp2 = []
        increase = False
        while len(temp1) > 0:
            for node in temp1:
                if node.left is not None:
                    temp2.append(node.left)
                    if len(temp2) > 1 and increase and temp2[-1].val <= temp2[-2].val:
                        return False
                    elif len(temp2) > 1 and not increase and temp2[-1].val >= temp2[-2].val:
                        return False
                if node.right is not None:
                    temp2.append(node.right)
                    if len(temp2) > 1 and increase and temp2[-1].val <= temp2[-2].val:
                        return False
                    elif len(temp2) > 1 and not increase and temp2[-1].val >= temp2[-2].val:
                        return False
            increase = not increase
            temp1 = list(temp2)
            temp2.clear()
        return True