You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.dfs(root, 0)
        return self.total

    def dfs(self, node: Optional[TreeNode], value: int) -> None:
        if node:
            # left shift to make room for the current node's value
            value = (value << 1) | node.val
            # if the node is a leaf, add the path value to the total sum
            if node.left is None and node.right is None:
                self.total += value
            else:
                self.dfs(node.left, value)
                self.dfs(node.right, value)
