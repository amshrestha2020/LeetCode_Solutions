Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:


Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.
Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [0, 1000].
-109 <= Node.val <= 109
-1000 <= targetSum <= 1000





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numOfPaths = 0
        self.target = targetSum
        # prefix dict to save the prefix sum and its corresponding frequency
        self.prefix = dict()
        # prefix[0] = 1 is a dummy node to avoid the edge case if root.val == target
        self.prefix[0] = 1
        # DFS to find the total number of paths
        self.dfs(root, 0)
        return self.numOfPaths
    
    # the main dfs process
    def dfs(self, node, currPathSum):
        # exit condition
        if not node:
            return 
        # calculate the prefix sum
        currPathSum += node.val
        # here is the key, we need to find if there is a subarray sum equals to target
        self.numOfPaths += self.prefix.get(currPathSum - self.target, 0)
        # update the prefix sum dict
        self.prefix[currPathSum] = self.prefix.get(currPathSum, 0) + 1
        # explore the left subtree
        self.dfs(node.left, currPathSum)
        # explore the right subtree
        self.dfs(node.right, currPathSum)
        # restore the prefix sum dict
        self.prefix[currPathSum] -= 1
