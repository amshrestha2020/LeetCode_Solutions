Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return head
        
        current = head
        
        while current.next:
            # If the current node's value is equal to the next node's value, remove the next node
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next  # Move to the next node
        
        return head
