Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path, current_sum):
            if not node:
                return
            
            # Update the current path and sum
            path.append(node.val)
            current_sum += node.val
            
            # If it's a leaf node and the sum equals targetSum, add the path to the result
            if not node.left and not node.right and current_sum == targetSum:
                result.append(path[:])
            
            # Recursively traverse the left and right subtrees
            dfs(node.left, path, current_sum)
            dfs(node.right, path, current_sum)
            
            # Backtrack: remove the current node from the path
            path.pop()
        
        result = []
        dfs(root, [], 0)
        return result

