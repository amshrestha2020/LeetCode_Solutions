Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if the list is empty or has only one element
        if not head or not head.next:
            return head
        
        # Calculate the length of the list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        # Calculate the actual rotation amount
        k %= length
        if k == 0:
            return head
        
        # Find the new tail
        new_tail_index = length - k - 1
        new_tail = head
        for _ in range(new_tail_index):
            new_tail = new_tail.next
        
        # Rotate the list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head
        
        return new_head
