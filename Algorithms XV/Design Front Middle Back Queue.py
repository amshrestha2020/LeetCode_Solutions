Design a queue that supports push and pop operations in the front, middle, and back.

Implement the FrontMiddleBack class:

FrontMiddleBack() Initializes the queue.
void pushFront(int val) Adds val to the front of the queue.
void pushMiddle(int val) Adds val to the middle of the queue.
void pushBack(int val) Adds val to the back of the queue.
int popFront() Removes the front element of the queue and returns it. If the queue is empty, return -1.
int popMiddle() Removes the middle element of the queue and returns it. If the queue is empty, return -1.
int popBack() Removes the back element of the queue and returns it. If the queue is empty, return -1.
Notice that when there are two middle position choices, the operation is performed on the frontmost middle position choice. For example:

Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4, 5].
Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4, 5, 6].
 

Example 1:

Input:
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
Output:
[null, null, null, null, null, 1, 3, 4, 2, -1]

Explanation:
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // return 1 -> [4, 3, 2]
q.popMiddle();    // return 3 -> [4, 2]
q.popMiddle();    // return 4 -> [2]
q.popBack();      // return 2 -> []
q.popFront();     // return -1 -> [] (The queue is empty)
 

Constraints:

1 <= val <= 109
At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront, popMiddle, and popBack.


class FrontMiddleBackQueue:
    from collections import deque

    def __init__(self):
        # Using deque to maintain the queue structure
        self.queue = deque()

    def pushFront(self, val: int) -> None:
        # Insert at the front
        self.queue.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        # Insert at the middle, middle index is len(queue) // 2
        mid = len(self.queue) // 2
        self.queue.insert(mid, val)

    def pushBack(self, val: int) -> None:
        # Insert at the back
        self.queue.append(val)

    def popFront(self) -> int:
        # Pop from the front, return -1 if queue is empty
        if not self.queue:
            return -1
        return self.queue.popleft()

    def popMiddle(self) -> int:
        # Check if the queue is empty first
        if not self.queue:
            return -1
        # Pop the middle element, if two middle elements, pop the first middle
        mid = (len(self.queue) - 1) // 2  # Calculate the middle index correctly
        middle_element = self.queue[mid]  # Get the middle element
        del self.queue[mid]               # Remove the element at the middle index
        return middle_element

    def popBack(self) -> int:
        # Pop from the back, return -1 if queue is empty
        if not self.queue:
            return -1
        return self.queue.pop()

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
