There is an exam room with n seats in a single row labeled from 0 to n - 1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.

Design a class that simulates the mentioned exam room.

Implement the ExamRoom class:

ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
int seat() Returns the label of the seat at which the next student will set.
void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.
 

Example 1:

Input
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
Output
[null, 0, 9, 4, 2, null, 5]

Explanation
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.

 

Constraints:

1 <= n <= 109
It is guaranteed that there is a student sitting at seat p.
At most 104 calls will be made to seat and leave.




class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.students = []

    def seat(self) -> int:
        # If no students, the student sits at seat number 0.
        if not self.students:
            student = 0
        else:
            # Compute the distance to the closest student and initialize the student to sit at 0.
            dist, student = self.students[0], 0
            # Loop over all students to find the maximum distance to the closest student.
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i - 1]
                    # Find the maximum distance to the closest student.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, student = d, prev + d
            # If the last seat can be assigned and is larger than dist, assign the student to the last seat.
            d = self.n - 1 - self.students[-1]
            if d > dist:
                student = self.n - 1

        # Add the student to our sorted list of students.
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        # Remove the student p from our sorted list of students.
        self.students.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
