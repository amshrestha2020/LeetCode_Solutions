You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.

Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.

You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.

Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.

 

Example 1:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2
Output: [1,2]
Explanation: 
Both the students have 1 positive feedback and 3 points but since student 1 has a lower ID he ranks higher.
Example 2:

Input: positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2
Output: [2,1]
Explanation: 
- The student with ID 1 has 1 positive feedback and 1 negative feedback, so he has 3-1=2 points. 
- The student with ID 2 has 1 positive feedback, so he has 3 points. 
Since student 2 has more points, [2,1] is returned.
 

Constraints:

1 <= positive_feedback.length, negative_feedback.length <= 104
1 <= positive_feedback[i].length, negative_feedback[j].length <= 100
Both positive_feedback[i] and negative_feedback[j] consists of lowercase English letters.
No word is present in both positive_feedback and negative_feedback.
n == report.length == student_id.length
1 <= n <= 104
report[i] consists of lowercase English letters and spaces ' '.
There is a single space between consecutive words of report[i].
1 <= report[i].length <= 100
1 <= student_id[i] <= 109
All the values of student_id[i] are unique.
1 <= k <= n





class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:

        from typing import List
        from collections import defaultdict


        positive_set = set(positive_feedback)
        negative_set = set(negative_feedback)
        
        # Dictionary to hold student points
        points = defaultdict(int)
        
        # Calculate points for each student based on their reports
        for r, sid in zip(report, student_id):
            words = r.split()
            for word in words:
                if word in positive_set:
                    points[sid] += 3
                elif word in negative_set:
                    points[sid] -= 1
        
        # Ensure every student ID is included, defaulting to 0 points if no feedback is received
        for sid in student_id:
            if sid not in points:
                points[sid] = 0
        
        # Sort students by points and student_id
        sorted_students = sorted(points.items(), key=lambda item: (-item[1], item[0]))
        
        # Get top k student IDs
        result = [sid for sid, _ in sorted_students[:k]]
        
        return result