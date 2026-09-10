# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0

        def avg(node):
            if not node:
                return 0,0

            left_val, left_count = avg(node.left)
            
            right_val, right_count = avg(node.right)

            new_val = left_val + right_val + node.val
            
            new_count = left_count + right_count + 1

            if new_val // new_count == node.val:
                self.result += 1
            return new_val, new_count

        avg(root)
        return self.result