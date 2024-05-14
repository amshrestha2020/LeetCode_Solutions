Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100



from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([(root, 0)])  # The queue contains pairs (node, level)
        rightmost_values = {}  # Dictionary to store the rightmost value at each level
        
        while queue:
            node, level = queue.popleft()
            
            # Overwrite the value at the current level (this will be the rightmost node at this level)
            rightmost_values[level] = node.val
            
            # Add the node's children to the queue
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # Return the rightmost values, in order from the top level to the bottom level
        return [rightmost_values[i] for i in range(len(rightmost_values))]

