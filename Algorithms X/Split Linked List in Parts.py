Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
Example 2:


Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
Output: [[1,2,3,4],[5,6,7],[8,9,10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
 

Constraints:

The number of nodes in the list is in the range [0, 1000].
0 <= Node.val <= 1000
1 <= k <= 50





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # Count the length of the linked list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part
        part_size, extra = divmod(length, k)
        
        # Initialize the result array
        parts = [None] * k
        current = head
        for i in range(k):
            if current:
                parts[i] = current
                size = part_size + (1 if i < extra else 0)
                for j in range(size - 1):
                    current = current.next
                next_head = current.next
                current.next = None
                current = next_head
        
        return parts

# Helper function to convert a list to a linked list
def list_to_linkedlist(elements: List[int]) -> ListNode:
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for element in elements[1:]:
        current.next = ListNode(element)
        current = current.next
    return head

# Helper function to print linked list parts
def print_linkedlist_parts(parts: List[ListNode]):
    for part in parts:
        current = part
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage
head = list_to_linkedlist([1, 2, 3])
k = 5
solution = Solution()
parts = solution.splitListToParts(head, k)
print_linkedlist_parts(parts)
