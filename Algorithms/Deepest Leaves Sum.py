Given the root of a binary tree, return the sum of values of its deepest leaves.
 

Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])  # The queue holds tuples of (node, depth)
        depth = -1  # The depth of the deepest level visited
        total = 0  # The sum of the node values at the deepest level

        while queue:
            node, level = queue.popleft()

            if level > depth:
                # We're visiting a deeper level, so we reset the total
                total = node.val
                depth = level
            elif level == depth:
                # We're still on the same level, so we add to the total
                total += node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return total
