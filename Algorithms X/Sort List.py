Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
 

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Base case: a list of zero or one node is sorted already

        # Step 1: Split the list into two halves
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None  # Cut the list in the middle

        # Step 2: Sort each half
        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 3: Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left: 'ListNode', right: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        curr = dummy
        while left and right:
            if left.val < right.val:
                curr.next, left = left, left.next
            else:
                curr.next, right = right, right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next