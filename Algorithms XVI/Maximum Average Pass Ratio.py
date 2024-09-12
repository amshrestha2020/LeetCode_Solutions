There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 

Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105





class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq
        from typing import List

        max_heap = []
        
        # Function to calculate potential gain from adding one student to a class
        def ratio_gain(p, t):
            # Current pass ratio
            current_ratio = p / t
            # New pass ratio if one student is added
            new_ratio = (p + 1) / (t + 1)
            # Gain in ratio
            return new_ratio - current_ratio
        
        # Initialize the heap with all classes
        for p, t in classes:
            # Push negative gain to make it a max-heap
            heapq.heappush(max_heap, (-ratio_gain(p, t), p, t))
        
        # Distribute extra students
        for _ in range(extraStudents):
            # Get the class with the maximum gain
            neg_gain, p, t = heapq.heappop(max_heap)
            # Update the class with one more student
            p += 1
            t += 1
            # Push the updated class back into the heap
            heapq.heappush(max_heap, (-ratio_gain(p, t), p, t))
        
        # Calculate the final average pass ratio
        total_ratio = 0
        while max_heap:
            _, p, t = heapq.heappop(max_heap)
            total_ratio += p / t
        
        return total_ratio / len(classes)