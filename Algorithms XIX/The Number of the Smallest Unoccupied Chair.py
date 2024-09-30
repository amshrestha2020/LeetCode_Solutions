There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

 

Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
 

Constraints:

n == times.length
2 <= n <= 104
times[i].length == 2
1 <= arrivali < leavingi <= 105
0 <= targetFriend <= n - 1
Each arrivali time is distinct.




class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def swap(self, frm, to):
        self.heap[frm], self.heap[to] = self.heap[to], self.heap[frm]

    def get_child_indexes(self, index):
        return {
            'left': index * 2 + 1,
            'right': index * 2 + 2,
        }

    def add(self, element):
        self.heap.append(element)
        current_working_index = len(self.heap) - 1
        while current_working_index > 0:
            parent_index = self.get_parent_index(current_working_index)
            if self.heap[parent_index] > self.heap[current_working_index]:
                self.swap(parent_index, current_working_index)
                current_working_index = parent_index
            else:
                break

    def remove(self):
        smallest_element = self.heap[0]
        if len(self.heap) == 1:
            self.heap = []
            return smallest_element
        last_element = self.heap.pop()
        self.heap[0] = last_element
        current_working_index = 0
        while True:
            child_indexes = self.get_child_indexes(current_working_index)
            left_child = self.heap[child_indexes['left']] if child_indexes['left'] < len(self.heap) else None
            right_child = self.heap[child_indexes['right']] if child_indexes['right'] < len(self.heap) else None
            if left_child is None and right_child is None:
                break
            if left_child is not None and right_child is not None:
                smallest_index = child_indexes['left'] if left_child < right_child else child_indexes['right']
            elif left_child is not None:
                smallest_index = child_indexes['left']
            else:
                smallest_index = child_indexes['right']
            if self.heap[smallest_index] < self.heap[current_working_index]:
                self.swap(smallest_index, current_working_index)
                current_working_index = smallest_index
            else:
                break
        return smallest_element


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        incoming_time_vs_outgoing_time_mapping = {}
        time_vs_chair_freeing = {}
        min_heap = MinHeap()

        for index in range(len(times)):
            min_heap.add(index)

        for index in range(len(times)):
            incoming_time_vs_outgoing_time_mapping[times[index][0]] = times[index][1]

        for index in range(max(incoming_time_vs_outgoing_time_mapping.keys()) + 1):
            # Freeing up the chair, because next person may sit on this chair itself
            if index in time_vs_chair_freeing:
                for iterator in time_vs_chair_freeing[index]:
                    min_heap.add(iterator)
                time_vs_chair_freeing[index] = []

            if index in incoming_time_vs_outgoing_time_mapping:
                chair_available = min_heap.remove()
                if index == times[targetFriend][0]:
                    return chair_available

                outgoing_time = incoming_time_vs_outgoing_time_mapping[index]
                if outgoing_time not in time_vs_chair_freeing:
                    time_vs_chair_freeing[outgoing_time] = []
                time_vs_chair_freeing[outgoing_time].append(chair_available)