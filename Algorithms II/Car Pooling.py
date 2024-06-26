There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105






import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort the trips by the start location
        trips.sort(key=lambda x: x[1])
        
        # Initialize a priority queue for the current passengers
        pq = []
        
        for trip in trips:
            num_passengers, start_location, end_location = trip
            
            # Pop out all trips that have ended before the current trip starts
            while pq and pq[0][0] <= start_location:
                _, passengers = heapq.heappop(pq)
                capacity += passengers
            
            # Check if the current trip can fit in the car
            if num_passengers > capacity:
                return False
            
            # Push the current trip into the priority queue
            heapq.heappush(pq, (end_location, num_passengers))
            
            # Update the capacity
            capacity -= num_passengers
        
        return True
