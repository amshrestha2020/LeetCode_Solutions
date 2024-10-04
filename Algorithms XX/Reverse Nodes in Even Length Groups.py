You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
Example 2:


Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
Example 3:


Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 105





# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head: ListNode, count: int) -> ListNode:
        prev = None
        cur = head
        next_node = None
        
        while cur is not None and count > 0:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            count -= 1
        
        head.next = next_node  # Connect the end of the reversed part to the next node
        return prev  # New head of the reversed list

    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        counter = 2  # Start from group size of 2
        cur = head.next  # Start from the second node
        prev = head  # Keep track of the previous node
        
        while cur is not None:
            l_curr = cur  # Copy of the current node
            l_prev = prev  # Copy of the previous node
            count = 1
            
            # Traverse to the end of the current group
            while cur is not None and count <= counter:
                prev = cur
                cur = cur.next
                count += 1
            
            count -= 1  # Adjust count to the actual number of nodes processed
            
            # If the number of nodes is even, reverse the group
            if count % 2 == 0:
                new_head = self.reverse(l_curr, count)  # Reverse the current group
                l_prev.next = new_head  # Connect the previous group to the new head
                prev = l_curr  # Update prev to the end of the reversed group
            
            counter += 1  # Increment the group size for the next group
        
        return head
        