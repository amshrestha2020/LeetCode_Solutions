You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

 

Example 1:


Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.
Example 2:


Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= n
All the values in the tree are unique.
1 <= startValue, destValue <= n
startValue != destValue



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            
            return False
        
        # Helper function to find the lowest common ancestor (LCA)
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        # Step 1: Find the LCA of startValue and destValue
        lca = findLCA(root, startValue, destValue)
        
        # Step 2: Find the path from LCA to startValue and LCA to destValue
        pathToStart = []
        pathToDest = []
        
        findPath(lca, startValue, pathToStart)
        findPath(lca, destValue, pathToDest)
        
        # Step 3: Convert the path from LCA to startValue to 'U' (up moves)
        #         All moves in pathToStart will be 'U' because we go up to the LCA
        result = ['U'] * len(pathToStart)
        
        # Step 4: Append the path from LCA to destValue (already in 'L'/'R')
        result.extend(pathToDest)
        
        return ''.join(result)        