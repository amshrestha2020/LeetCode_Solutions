You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 105
0 <= Node.val <= 100



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Step 2: Find the kth node from the beginning and the kth node from the end
        kth_from_start = head
        kth_from_end = head
        for _ in range(k - 1):
            kth_from_start = kth_from_start.next
        
        for _ in range(length - k):
            kth_from_end = kth_from_end.next
        
        # Step 3: Swap the values of the two nodes
        kth_from_start.val, kth_from_end.val = kth_from_end.val, kth_from_start.val
        
        # Step 4: Return the modified linked list
        return head        