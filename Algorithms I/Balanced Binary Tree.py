Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_balance(self, root):
        if not root:
            return True, 0
        
        left_balanced, left_height = self.check_balance(root.left)
        right_balanced, right_height = self.check_balance(root.right)
        
        if not left_balanced or not right_balanced or abs(left_height - right_height) > 1:
            return False, 0
        
        return True, max(left_height, right_height) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check_balance(root)[0]
