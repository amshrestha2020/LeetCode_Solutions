You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105





import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by their start day
        events.sort(key=lambda x: x[0])
        
        # Min-heap to keep track of end days of available events
        min_heap = []
        max_events = 0
        i, n = 0, len(events)
        day = 0
        
        while i < n or min_heap:
            if not min_heap:
                # If heap is empty, move to the next available event start day
                day = events[i][0]
            
            # Add all events starting today to the heap
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            
            # Attend the event that ends the earliest
            heapq.heappop(min_heap)
            max_events += 1
            day += 1
            
            # Remove all events from heap that have already ended
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
        
        return max_events


