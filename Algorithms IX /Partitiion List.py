Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
 

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Initialize two dummy nodes as the heads of the two linked lists.
        before_head = ListNode(0)
        after_head = ListNode(0)
        
        before = before_head  # Pointer for the first list
        after = after_head  # Pointer for the second list
        
        while head:
            if head.val < x:
                # Insert node into the first list
                before.next = head
                before = before.next
            else:
                # Insert node into the second list
                after.next = head
                after = after.next
            
            # Move ahead in the original list
            head = head.next
        
        # Important: disconnect the second list from the rest of the nodes to avoid a cycle
        after.next = None
        # Connect the two lists
        before.next = after_head.next
        
        return before_head.next
