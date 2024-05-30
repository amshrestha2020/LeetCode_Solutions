Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:



Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
Example 2:



Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.
Example 3:

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.
 

Constraints:

The number of nodes in the tree is in the range [1, 4 * 104].
-4 * 104 <= Node.val <= 4 * 104




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        def traverse(node):
            # Returns:
            #   is_bst: True if the subtree rooted at this node is a BST
            #   bst_sum: The sum of all nodes in the BST rooted at this node
            #   min_val: The minimum value in the subtree rooted at this node
            #   max_val: The maximum value in the subtree rooted at this node
            if not node:
                return True, 0, float('inf'), float('-inf')
            left_is_bst, left_bst_sum, left_min_val, left_max_val = traverse(node.left)
            right_is_bst, right_bst_sum, right_min_val, right_max_val = traverse(node.right)
            if left_is_bst and right_is_bst and left_max_val < node.val < right_min_val:
                bst_sum = node.val + left_bst_sum + right_bst_sum
                self.max_sum = max(self.max_sum, bst_sum)
                return True, bst_sum, min(left_min_val, node.val), max(right_max_val, node.val)
            else:
                return False, 0, 0, 0
        traverse(root)
        return self.max_sum
