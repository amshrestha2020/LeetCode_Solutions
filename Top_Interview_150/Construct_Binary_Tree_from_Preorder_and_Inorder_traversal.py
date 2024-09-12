Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            if in_left == in_right:
                return None
            
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            index = idx_map[root_val]

            pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index + 1, in_right)
            return root
        
        pre_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper()
