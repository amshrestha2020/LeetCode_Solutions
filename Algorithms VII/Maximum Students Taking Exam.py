Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible.

Students must be placed in seats in good condition.

 

Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
 

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8



class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        valid = [0] * m
        for i in range(m):
            for j in range(n):
                valid[i] = (valid[i] << 1) + (seats[i][j] == '.')

        dp = [-1] * (1 << n)
        dp[0] = 0

        for i in range(m):
            dp2 = [-1] * (1 << n)
            for j in range(1 << n):
                if (j & valid[i]) == j and not (j & (j >> 1)):
                    for k in range(1 << n):
                        if dp[k] != -1 and not (j & (k >> 1)) and not ((j >> 1) & k):
                            dp2[j] = max(dp2[j], dp[k] + bin(j).count('1'))
            dp = dp2

        return max(dp)
