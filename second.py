# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_level_sum = root.val
        max_level = 1
        curr_level = [root]
        next_level = []
        level = 1
        while len(curr_level) != 0:
            level_sum = 0
            for node in curr_level:
                level_sum += node.val
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
            curr_level = list(next_level)
            level += 1
            next_level.clear()
        return max_level


if __name__ == '__main__':
    root = TreeNode(-100)
    root.left = TreeNode(-200)
    root.right = TreeNode(-300)
    root.left.left = TreeNode(-20)
    root.left.right = TreeNode(-5)
    root.right.left = TreeNode(-10)
    s = Solution()
    print(s.maxLevelSum(root))
