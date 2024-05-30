Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_middle(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None  # Split the list into two halves
        return slow
    
    def sortedListToBSTHelper(self, head):
        if not head:
            return None
        
        mid = self.find_middle(head)
        root = TreeNode(mid.val)
        
        if head == mid:  # If there's only one node in the linked list
            return root
        
        root.left = self.sortedListToBSTHelper(head)
        root.right = self.sortedListToBSTHelper(mid.next)
        
        return root
    
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.sortedListToBSTHelper(head)
