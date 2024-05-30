Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1




# Definition for a binary tree node.
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        # BFS initialization
        queue = deque([root])
        largest_values = []
        
        while queue:
            level_size = len(queue)
            level_max = float('-inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            largest_values.append(level_max)
        
        return largest_values

# Example usage:
# Constructing the tree [1,3,2,5,3,null,9]
#       1
#      / \
#     3   2
#    / \   \
#   5   3   9
root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)

solution = Solution()
print(solution.largestValues(root))  # Output: [1, 3, 9]
