There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

 

Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0
 

Constraints:

1 <= courses.length <= 104
1 <= durationi, lastDayi <= 104





import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort the courses by their ending day
        courses.sort(key=lambda x: x[1])
        
        # Initialize a max heap to keep track of the longest courses
        max_heap = []
        curr_time = 0
        
        for course in courses:
            duration, end_day = course
            # Add the course to the current schedule
            heapq.heappush(max_heap, -duration)
            curr_time += duration
            
            # If adding the current course makes us miss a deadline, 
            # remove the longest course
            while curr_time > end_day:
                curr_time += heapq.heappop(max_heap)
        
        # The size of the heap is the maximum number of courses that can be taken
        return len(max_heap)

