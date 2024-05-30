On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.







class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        # Flatten the board and find the index of 0
        flat_board = [num for sublist in board for num in sublist]
        if 0 in flat_board:
            moves, used, cnt = deque([(flat_board, flat_board.index(0))]), set([str(flat_board)]), 0
        else:
            print("0 is not in the board")
            return -1
        final = [1, 2, 3, 4, 5, 0]
        while moves:
            for _ in range(len(moves)):
                curr, zero = moves.popleft()
                if curr == final: return cnt
                for d in (-1, 1, -3, 3):
                    next_zero = zero + d
                    if abs(zero // 3 - next_zero // 3) + abs(zero % 3 - next_zero % 3) != 1:
                        continue
                    if 0 <= next_zero < 6:
                        new_board = curr[:]
                        new_board[zero], new_board[next_zero] = new_board[next_zero], new_board[zero]
                        if str(new_board) not in used:
                            used.add(str(new_board))
                            moves.append((new_board, next_zero))
            cnt += 1
        return -1
