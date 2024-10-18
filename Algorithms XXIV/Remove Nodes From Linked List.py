You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        # Step 1: Reverse the linked list
        reversed_head = reverse(head)
        
        # Step 2: Traverse reversed list and remove nodes
        max_val = float('-inf')
        dummy = ListNode(0)  # Dummy node to help rebuild the list
        new_head = dummy
        current = reversed_head
        
        while current:
            if current.val >= max_val:
                max_val = current.val
                new_head.next = current
                new_head = new_head.next
            current = current.next
        
        # Step 3: Reverse the list again to restore original order
        new_head.next = None  # End the list properly
        return reverse(dummy.next)