In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6





class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # Calculate the level of the given label
        level = 0
        while (1 << level) <= label:
            level += 1
        
        path = []
        
        # Work backwards from the given label to the root
        while label > 0:
            path.append(label)
            max_val_in_level = (1 << level) - 1
            min_val_in_level = (1 << (level - 1))
            label = (max_val_in_level + min_val_in_level - label) // 2
            level -= 1
        
        # Reverse to get the path from root to the given label
        path.reverse()
        return path