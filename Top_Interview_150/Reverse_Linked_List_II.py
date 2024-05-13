Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None

        # Create a dummy node to mark the head of this list
        dummy = ListNode(0)
        dummy.next = head

        # Make a pointer pre as a marker for the node before reversing
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next

        # A pointer to the beginning of a sub-list that will be reversed
        start = pre.next

        # A pointer to a node that will be reversed
        then = start.next

        # Reverse the sub-list
        for _ in range(right - left):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return dummy.next

        