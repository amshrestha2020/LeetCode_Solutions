You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106




class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import heapq
        from sortedcontainers import SortedList
        
        n = len(events)
        
        # Step 1: Sort events by their start time (and end time as tie breaker)
        events.sort()
        
        # Step 2: Use a sorted list (like multiset) to store event values
        s = SortedList()
        maxi = [float('-inf')] * (n + 1)
        maxi[n] = 0  # Base case
        
        # Insert the last event value to set up for calculations
        s.add(events[n-1][2])
        maxi[n-1] = events[n-1][2]
        
        # Step 3: Compute the next valid non-overlapping event for each event
        next_event = [-1] * n
        pq = []
        
        for i in range(n):
            # Process the priority queue to find non-overlapping events
            while pq:
                end_time, idx = pq[0]
                if end_time < events[i][0]:
                    heapq.heappop(pq)
                    next_event[idx] = i
                else:
                    break
            heapq.heappush(pq, (events[i][1], i))
        
        # For remaining events in the priority queue, mark them as non-overlapping with any future event
        while pq:
            end_time, idx = heapq.heappop(pq)
            next_event[idx] = n
        
        # Step 4: Find the maximum sum of two non-overlapping events
        ans = events[n-1][2]
        
        for i in range(n-2, -1, -1):
            index = next_event[i]
            ans = max(ans, events[i][2] + maxi[index])
            maxi[i] = max(events[i][2], s[-1])
            s.add(events[i][2])
        
        return ans